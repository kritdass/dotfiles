from libqtile import widget, bar
from libqtile.lazy import lazy
from qtile_extras import widget
import os
from utils.settings import colors, font, fontsize

widget_defaults = dict(
    font=font,
    fontsize=fontsize,
    padding=3,
    foreground=colors["foreground"],
    background=colors["background"],
)


def parse_window(w):
    for name in ["Brave", "Discord", "Slack", "NVIM"]:
        if name in w:
            return name + " - " + w.replace(" - " + name, "")
    return w


def top_bar():
    return bar.Bar(
        [
            widget.Spacer(length=10),
            widget.TextBox(
                text="",
                fontsize=25,
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                padding=5,
            ),
            widget.WindowName(
                max_chars=25,
                empty_group_string="Desktop",
                width=275,
                scroll=True,
                parse_text=parse_window,
                format="{name}",
            ),
            widget.Spacer(),
            widget.GroupBox(
                highlight_method="line",
                this_current_screen_border=colors["foreground"],
                spacing=10,
                fontsize=28,
                active=colors["foreground"],
                inactive=colors["white"],
                highlight_color=colors["background"],
            ),
            widget.Spacer(),
            widget.Clock(
                format=" %B %d",
            ),
            widget.Clock(format="%l:%M %p", padding=18),
            widget.UPowerWidget(
                text_charging="{percentage:.0f}%",
                text_discharging="{percentage:.0f}%",
                battery_height=12,
                fill_normal=colors["foreground"],
                border_colour=colors["foreground"],
                border_charge_colour=colors["foreground"],
            ),
            widget.Battery(format="{percent:2.0%}"),
            widget.TextBox(
                text="󰐥",
                fontsize=26,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        "rofi -show power-menu -modi power-menu:"
                        + os.path.expanduser("~/.local/bin/rofi-power-menu")
                    )
                },
                padding=12,
            ),
            widget.Spacer(length=5),
        ],
        50,
        background="#00000000",
        opacity=1,
        margin=[10, 10, 0, 10],
    )
