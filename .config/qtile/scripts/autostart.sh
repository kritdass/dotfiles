#!/usr/bin/env bash

picom -b &
dunst &
flameshot &

if [[ $(cat ~/.config/theme.txt) == *"dark"** ]]; then
	xrdb merge ~/.config/.Xresources.dark && kill -USR1 $(pidof st)
elif [[ $(cat ~/.config/theme.txt) == *"light"** ]]; then
	xrdb merge ~/.config/.Xresources.light && kill -USR1 $(pidof st)
fi
