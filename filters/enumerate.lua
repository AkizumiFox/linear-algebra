--[[
Labeled Lists Filter
====================
Handles enumitem-style labels on ordered lists:

    ::: {.enumerate options="label=(VS\arabic*)"}
    1. ...
    :::

LaTeX: \begin{enumerate}[label=(VS\arabic*)] ... \end{enumerate}
HTML:  <ol class="labeled-list"> with an explicit label span in each item.
]]

local COUNTER_STYLES = {
    arabic = function(n) return tostring(n) end,
    alph = function(n) return string.char(96 + n) end,
    Alph = function(n) return string.char(64 + n) end,
    roman = function(n) return pandoc.utils.to_roman_numeral(n):lower() end,
    Roman = function(n) return pandoc.utils.to_roman_numeral(n) end,
}

-- Split "label=(VS\arabic*)" into prefix "(VS", style "arabic", suffix ")"
local function parse_label(options)
    local label = options:match("label%s*=%s*{(.-)}%s*$") or options:match("label%s*=%s*([^,]+)")
    if not label then return nil end
    local prefix, style, suffix = label:match("^(.-)\\(%a+)%*(.*)$")
    if not prefix or not COUNTER_STYLES[style] then return nil end
    return {raw = label, prefix = prefix, style = style, suffix = suffix}
end

local function Div(div)
    if not div.classes:includes("enumerate") then return nil end
    local options = div.attributes["options"]
    if not options then return nil end
    local label = parse_label(options)
    if not label then
        io.stderr:write("Warning: unsupported enumerate options: " .. options .. "\n")
        return nil
    end

    -- Only the single-list case is supported; anything else is left for other filters
    if #div.content ~= 1 or div.content[1].t ~= "OrderedList" then
        io.stderr:write("Warning: .enumerate div must contain exactly one numbered list\n")
        return nil
    end
    local list = div.content[1]
    local start = list.listAttributes.start or 1

    if FORMAT:match("latex") then
        local blocks = {pandoc.RawBlock("latex", "\\begin{enumerate}[label=" .. label.raw .. "]")}
        if start ~= 1 then
            table.insert(blocks, pandoc.RawBlock("latex", string.format("\\setcounter{enumi}{%d}", start - 1)))
        end
        for _, item in ipairs(list.content) do
            table.insert(blocks, pandoc.RawBlock("latex", "\\item"))
            for _, block in ipairs(item) do
                table.insert(blocks, block)
            end
        end
        table.insert(blocks, pandoc.RawBlock("latex", "\\end{enumerate}"))
        return blocks
    end

    if FORMAT:match("html") then
        local items = {}
        for i, item in ipairs(list.content) do
            local text = label.prefix .. COUNTER_STYLES[label.style](start + i - 1) .. label.suffix
            local marker = pandoc.Span({pandoc.Str(text)}, pandoc.Attr("", {"item-label"}))
            local blocks = pandoc.Blocks(item)
            local first = blocks[1]
            if first and (first.t == "Plain" or first.t == "Para") then
                first.content:insert(1, pandoc.Space())
                first.content:insert(1, marker)
            else
                blocks:insert(1, pandoc.Plain({marker}))
            end
            table.insert(items, blocks)
        end
        local bullet = pandoc.BulletList(items)
        return pandoc.Div({bullet}, pandoc.Attr("", {"labeled-list"}))
    end

    return nil
end

return {
    { Div = Div }
}
