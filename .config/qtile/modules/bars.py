from libqtile import widget, bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import os
from utils.settings import colors


def parse_window(w):
    for name in ["Brave", "Discord", "Slack", "NVIM"]:
        if name in w:
            return name + " - " + w.replace(" - " + name, "")
    return w


rounded = {
    "decorations": [
        RectDecoration(
            filled=True,
            clip=True,
            extrawidth=5,
            group=True,
            radius=15,
            use_widget_background=True,
            line_colour=colors["white"],
            line_width=1,
        )
    ]
}

sep = [
    widget.Spacer(length=3, background=colors["background"], **rounded),
    widget.Sep(size_percent=50, background=colors["background"], **rounded),
    widget.Spacer(length=5, background=colors["background"], **rounded),
]


def top_bar():
    return bar.Bar(
        [
            widget.Spacer(length=10, **rounded, background=colors["background"]),
            widget.TextBox(
                text=" ",
                fontsize=25,
                mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                background=colors["background"],
                padding=0,
                **rounded
            ),
            widget.WindowName(
                max_chars=25,
                empty_group_string="Desktop",
                width=275,
                scroll=True,
                parse_text=parse_window,
                format="{name}",
                background=colors["background"],
                **rounded
            ),
            widget.Spacer(length=7, **rounded, background=colors["background"]),
            widget.Spacer(),
            widget.Spacer(length=10, background=colors["background"], **rounded),
            widget.GroupBox(
                highlight_method="line",
                this_current_screen_border=colors["foreground"],
                spacing=10,
                fontsize=30,
                background=colors["background"],
                active=colors["foreground"],
                inactive=colors["white"],
                highlight_color=colors["background"],
                **rounded
            ),
            widget.Spacer(length=5, background=colors["background"], **rounded),
            widget.Spacer(),
            widget.Spacer(length=10, background=colors["background"], **rounded),
            widget.Clock(format=" %B %d", background=colors["background"], **rounded),
            *sep,
            widget.Clock(
                format=" %l:%M %p", background=colors["background"], **rounded
            ),
            widget.Spacer(length=5, background=colors["background"], **rounded),
            widget.Spacer(length=8),
            widget.Spacer(length=10, background=colors["background"], **rounded),
            widget.UPowerWidget(
                text_charging="{percentage:.0f}%",
                text_discharging="{percentage:.0f}%",
                battery_height=12,
                background=colors["background"],
                fill_normal=colors["foreground"],
                border_colour=colors["foreground"],
                **rounded
            ),
            widget.TextBox(
                text="󰐥",
                fontsize=25,
                mouse_callbacks={
                    "Button1": lazy.spawn(
                        "rofi -show power-menu -modi power-menu:"
                        + os.path.expanduser("~/.local/bin/rofi-power-menu")
                    )
                },
                background=colors["background"],
                padding=0,
                **rounded
            ),
            widget.Spacer(length=5, background=colors["background"], **rounded),
        ],
        40,
        background="#00000000",
        opacity=1,
        margin=[10, 10, 0, 10],
    )
