from libqtile.config import Screen
from modules.bars import top_bar
from utils.settings import colors, wallpaper, font, fontsize

widget_defaults = dict(
    font=font,
    fontsize=fontsize,
    padding=3,
    foreground=colors["foreground"],
    background=colors["background"]
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=top_bar(),
        wallpaper=wallpaper,
        wallpaper_mode="fill",
    ),
    Screen(top=top_bar(), wallpaper=wallpaper, wallpaper_mode="fill"),
]
