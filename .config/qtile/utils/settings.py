import os

mod = "mod4"
terminal = "wezterm"

font = "Fira Code Nerd Font Propo Ret"
fontsize = 16

with open(os.path.expanduser("~/.config/theme.txt"), "r") as theme:
    if "dark" in theme.readline():
        colors = {
            "background": "282c34",
            "foreground": "abb2bf",
            "black": "5c6370",
            "red": "e06c75",
            "green": "98c379",
            "yellow": "d19a66",
            "blue": "61afef",
            "magenta": "c678dd",
            "cyan": "56b6c2",
            "white": "828791",
        }
        wallpaper = os.path.expanduser("~/.config/qtile/assets/wallpaper_dark.jpg")
    else:
        colors = {
            "background": "faf4ed",
            "foreground": "797593",
            "black": "5c6370",
            "red": "b4637a",
            "green": "286983",
            "yellow": "ea9d34",
            "blue": "56949f",
            "magenta": "907aa9",
            "cyan": "d7827e",
            "white": "cecacd",
        }
        wallpaper = os.path.expanduser("~/.config/qtile/assets/wallpaper_light.jpg")

workspaces = [
    ("", terminal),
    ("", "brave"),
    ("󰭹", "discord"),
    ("󰝰", "thunar"),
    ("󰓇", "spotify"),
    ("󰊢", "gitkraken"),
    ("󰒱", "slack"),
]
