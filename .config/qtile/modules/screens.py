from libqtile.config import Screen
from modules.bars import top_bar, widget_defaults
from utils.settings import wallpaper

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=top_bar(),
        wallpaper=wallpaper,
        wallpaper_mode="fill",
    ),
    Screen(top=top_bar(), wallpaper=wallpaper, wallpaper_mode="fill"),
]
