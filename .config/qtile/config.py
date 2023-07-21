from libqtile import hook
import subprocess
import os
from modules.groups import groups
from modules.keys import keys
from modules.layouts import layouts, floating_layout
from modules.screens import screens, widget_defaults

dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_minimize = False
wmname = "qtile"


@hook.subscribe.startup_once
def start_once():
    subprocess.call([os.path.expanduser("~/.config/qtile/scripts/autostart.sh")])

print(layouts, floating_layout, screens, groups, keys, widget_defaults)

