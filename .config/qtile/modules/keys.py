from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy
from utils.settings import mod, terminal
import subprocess
import os


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        [mod],
        "q",
        lazy.spawn(
            "rofi -show power-menu -modi power-menu:"
            + os.path.expanduser("~/.local/bin/rofi-power-menu")
        ),
        desc="Launch rofi powermenu",
    ),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn rofi"),
    Key([mod], "m", lazy.window.toggle_minimize(), desc="Minimizes active window"),
    Key([mod, "control"], "s", lazy.spawn("flameshot gui"), desc="Takes a screenshot"),
    Key([mod], "f", lazy.spawn("brave"), desc="Opens browser"),
    Key([mod], "a", lazy.screen.next_group(), desc="Goes to the next group"),
    Key([mod], "z", lazy.screen.prev_group(), desc="Goes to the previous group"),
    Key(
        [mod],
        "t",
        lazy.spawn(
            "sh " + os.path.expanduser("~/.config/qtile/scripts/theme_switcher.sh")
        ),
        desc="Switch between dark and light themes",
    ),
    Key([mod], "s", lazy.next_screen(), desc="Switch the screen in focus"),
]
