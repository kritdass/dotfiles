#!/usr/bin/env bash

if [[ $(cat ~/.config/theme.txt) == *"dark"* ]]; then
	echo "light" >~/.config/theme.txt
	sed -i "s/Whitesur-onedark-dark/rose-pine-dawn-gtk/gi" ~/.xsettingsd
	sed -i "s/1e2127/faf4ed/gi" ~/.config/dunst/dunstrc
	sed -i "s/abb2bf/797593/gi" ~/.config/dunst/dunstrc
	cat ~/.config/Vencord/settings/light.css >~/.config/Vencord/settings/quickCss.css
	sed -i "s/dark.rasi/light.rasi/gi" ~/.config/rofi/config.rasi
	gsettings set org.gnome.desktop.interface color-scheme prefer-light
	xsettingsd -c ~/.config/.xsettingsd.light
elif [[ $(cat ~/.config/theme.txt) == *"light"* ]]; then
	echo "dark" >~/.config/theme.txt
	sed -i "s/rose-pine-dawn-gtk/Whitesur-onedark-dark/gi" ~/.xsettingsd
	sed -i "s/faf4ed/1e2127/gi" ~/.config/dunst/dunstrc
	sed -i "s/797593/abb2bf/gi" ~/.config/dunst/dunstrc
	cat ~/.config/Vencord/settings/dark.css >~/.config/Vencord/settings/quickCss.css
	sed -i "s/light.rasi/dark.rasi/gi" ~/.config/rofi/config.rasi
	gsettings set org.gnome.desktop.interface color-scheme prefer-dark
	xsettingsd -c ~/.config/.xsettingsd.dark
fi

echo "" >>~/.wezterm.lua
sed -i "$ d" ~/.wezterm.lua

qtile cmd-obj -o cmd -f reload_config

killall dunst
dunst

killall Discord
qtile run-cmd -g "3" discord
