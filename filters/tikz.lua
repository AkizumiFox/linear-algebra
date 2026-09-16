--[[
TikZ Filter
===========
LaTeX output keeps raw TikZ blocks as they are.

HTML output drops raw LaTeX, so each block containing a tikzpicture or tikzcd
environment is replaced by an <img> of tikz/<hash>.svg. The picture source is
written to <tikz-cache-dir>/<hash>.tex; build/tikz.py compiles those files to SVG
after the Pandoc run (no LaTeX is run from inside the filter).
]]

if not FORMAT:match("html") then
    return {}
end

local cache_dir = nil
local asset_prefix = "./"

local PICTURE_ENVS = { "tikzpicture", "tikzcd" }

-- Return the text from the first \begin{env} to the last matching \end{env}, or nil
local function extract_picture(text)
    for _, env in ipairs(PICTURE_ENVS) do
        local first = text:find("\\begin{" .. env .. "}", 1, true)
        if first then
            local last_end = nil
            local search_from = 1
            local closing = "\\end{" .. env .. "}"
            while true do
                local s, e = text:find(closing, search_from, true)
                if not s then break end
                last_end = e
                search_from = e + 1
            end
            if last_end then
                return text:sub(first, last_end)
            end
        end
    end
    return nil
end

local function write_source(hash, picture)
    local path = cache_dir .. "/" .. hash .. ".tex"
    local existing = io.open(path, "r")
    if existing then
        existing:close()
        return
    end
    local f = io.open(path, "w")
    if not f then
        io.stderr:write("Warning: cannot write TikZ source to " .. path .. "\n")
        return
    end
    f:write(picture)
    f:close()
end

local function RawBlock(block)
    if block.format ~= "tex" and block.format ~= "latex" then return nil end
    local picture = extract_picture(block.text)
    if not picture then return nil end

    local hash = pandoc.utils.sha1(picture)
    write_source(hash, picture)

    local image = pandoc.Image({}, asset_prefix .. "tikz/" .. hash .. ".svg", "",
        pandoc.Attr("", {"tikz"}, {}))
    return pandoc.Div({pandoc.Plain({image})}, pandoc.Attr("", {"tikz-figure"}, {}))
end

local function Meta(meta)
    if meta["tikz-cache-dir"] then
        cache_dir = pandoc.utils.stringify(meta["tikz-cache-dir"])
    end
    if meta["asset-prefix"] then
        asset_prefix = pandoc.utils.stringify(meta["asset-prefix"])
    end
end

return {
    { Meta = Meta },
    { RawBlock = function(block)
        if not cache_dir then return nil end
        return RawBlock(block)
    end },
}
