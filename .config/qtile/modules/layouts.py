from libqtile import layout
from libqtile.config import Match
from utils.settings import colors

layout_defaults = {"margin": 10, "border_focus": colors["white"]}

layouts = [
    layout.Columns(**layout_defaults, border_width=1),
    layout.Max(**layout_defaults, border_width=0),
]

floating_layout = layout.Floating(
    **layout_defaults,
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
