--[[
Macros Lua Filter for Pandoc
=============================
Expands LaTeX-style macros for consistent rendering in HTML.

For HTML output, injects macros into MathJax configuration.
For LaTeX output, macros are handled natively.

Author: Generated for Aaron Lin's Linear Algebra book project
]]

-- =============================================================================
-- Macro Parsing
-- =============================================================================

-- Extract balanced-brace content; returns (inner_content, position_after_closing_brace)
local function extract_braces(s, start)
    if s:sub(start, start) ~= "{" then return nil, start end
    local depth = 1
    local i = start + 1
    while i <= #s and depth > 0 do
        local c = s:sub(i, i)
        if c == "{" then depth = depth + 1
        elseif c == "}" then depth = depth - 1
        end
        i = i + 1
    end
    if depth ~= 0 then return nil, start end
    return s:sub(start + 1, i - 2), i
end

-- Parse \def\cmd{replacement} and \newcommand{\cmd}{replacement} from a file
-- Handles nested braces in replacement (e.g. \def\nR{\mathbb{R}})
local function parse_macros(content)
    local macros = {}

    -- \def \cmd {replacement}
    local pos = 1
    while true do
        local def_s, def_e = content:find("\\def%s*\\\\", pos)
        if not def_s then break end
        local cmd_s = def_e + 1
        local cmd_e = cmd_s
        while cmd_e <= #content and content:sub(cmd_e, cmd_e):match("%w") do
            cmd_e = cmd_e + 1
        end
        local cmd = content:sub(cmd_s, cmd_e - 1)
        local brace = content:find("{", cmd_e, true)
        if brace then
            local replacement, _ = extract_braces(content, brace)
            if replacement then
                macros[cmd] = replacement
            end
        end
        pos = def_s + 1
    end

    -- \newcommand{\cmd}{replacement}
    pos = 1
    while true do
        local start = content:find("\\newcommand%s*{", pos)
        if not start then break end
        local brace = content:find("{", start, true)
        if brace then
            local cmd, after_cmd = extract_braces(content, brace)
            if cmd then
                local rep_brace = content:find("{", after_cmd, true)
                if rep_brace then
                    local replacement, _ = extract_braces(content, rep_brace)
                    if replacement then macros[cmd] = replacement end
                end
            end
        end
        pos = start + 1
    end

    -- \providecommand{\cmd}{replacement}
    pos = 1
    while true do
        local start = content:find("\\providecommand%s*{", pos)
        if not start then break end
        local brace = content:find("{", start, true)
        if brace then
            local cmd, after_cmd = extract_braces(content, brace)
            if cmd and not macros[cmd] then
                local rep_brace = content:find("{", after_cmd, true)
                if rep_brace then
                    local replacement, _ = extract_braces(content, rep_brace)
                    if replacement then macros[cmd] = replacement end
                end
            end
        end
        pos = start + 1
    end

    return macros
end

-- =============================================================================
-- MathJax Configuration Generation
-- =============================================================================

local function generate_mathjax_macros(macros)
    local parts = {}
    
    -- Sorted so the generated page is identical between builds
    local names = {}
    for cmd in pairs(macros) do table.insert(names, cmd) end
    table.sort(names)
    for _, cmd in ipairs(names) do
        local replacement = macros[cmd]
        -- MathJax doesn't support \mathbbmss (bbm); use \mathbb as fallback
        replacement = replacement:gsub("\\mathbbmss", "\\mathbb")
        -- Escape backslashes for JavaScript
        local escaped = replacement:gsub("\\", "\\\\")
        table.insert(parts, string.format('            "%s": "%s"', cmd, escaped))
    end
    
    local macro_defs = table.concat(parts, ",\n")
    
    -- Merge into existing MathJax config (template sets it first)
    return string.format([[
<script>
(function(){
  if (typeof window.MathJax === 'undefined') window.MathJax = {};
  if (typeof window.MathJax.tex === 'undefined') window.MathJax.tex = {};
  if (typeof window.MathJax.tex.macros === 'undefined') window.MathJax.tex.macros = {};
  Object.assign(window.MathJax.tex.macros, {
%s
  });
})();
</script>
]], macro_defs)
end

-- =============================================================================
-- Filter
-- =============================================================================

local macros_injected = false

local function inject_macros(meta)
    if macros_injected then return nil end
    if not FORMAT:match("html") then return nil end
    
    -- Read macros file path from metadata
    local project_root = meta["project-root"]
    if not project_root then return nil end
    
    local macros_file = pandoc.utils.stringify(project_root) .. "/latex/macros.tex"
    
    -- Read file
    local f = io.open(macros_file, "r")
    if not f then
        io.stderr:write("Warning: Could not read macros file: " .. macros_file .. "\n")
        return nil
    end
    
    local content = f:read("*all")
    f:close()
    
    -- Parse macros
    local macros = parse_macros(content)
    
    -- Generate MathJax config
    local mathjax_config = generate_mathjax_macros(macros)
    
    -- Add to header-includes
    local header_includes = meta["header-includes"] or pandoc.MetaList({})
    if header_includes.t ~= "MetaList" then
        header_includes = pandoc.MetaList({header_includes})
    end
    
    table.insert(header_includes, pandoc.MetaBlocks({
        pandoc.RawBlock("html", mathjax_config)
    }))
    
    meta["header-includes"] = header_includes
    macros_injected = true
    
    return meta
end

return {
    {Meta = inject_macros}
}
