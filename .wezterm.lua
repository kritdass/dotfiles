local wezterm = require("wezterm")
local act = wezterm.action

local config = {}

if wezterm.config_builder then
	config = wezterm.config_builder()
end

config.keys = {
	{ key = "V", mods = "CTRL", action = act.PasteFrom("Clipboard") },
	{ key = "V", mods = "CTRL", action = act.PasteFrom("PrimarySelection") },
}

config.font = wezterm.font("JetFlow")
config.font_size = 13
config.enable_tab_bar = false
config.warn_about_missing_glyphs = false

local function read(strCmd)
	local hFile = assert(io.popen(strCmd, "r"))
	local strOutput = assert(hFile:read("*a"))
	hFile:close()

	return strOutput
end

local theme = read("strings ~/.config/theme.txt")
if string.find(theme, "dark") then
	config.color_scheme = "OneDark (base16)"
elseif string.find(theme, "light") then
	config.color_scheme = "Rosé Pine Dawn (base16)"
end

local padding = 30
config.window_padding = {
	left = padding,
	right = padding,
	top = padding,
	bottom = padding,
}

return config


