from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy
from modules.keys import keys, mod
from utils.settings import workspaces, terminal

groups = []

for i, workspace in enumerate(workspaces):
    i = str(i + 1)
    groups.append(
        Group(
            i,
            spawn=workspace[1],
            label=workspace[0],
        )
    )
    keys.extend(
        [
            Key(
                [mod],
                i,
                lazy.group[i].toscreen(),
                desc=f"Switch to group {i}",
            ),
            Key(
                [mod, "shift"],
                i,
                lazy.window.togroup(i, switch_group=True),
                desc=f"Switch to and move focused window to group {i}",
            ),
        ]
    )

dropdown_defaults = {"width": 0.8, "height": 0.8, "x": 0.1, "y": 0.1, "opacity": 1}

groups.append(
    ScratchPad(
        "scratchpad",
        [DropDown("term", terminal, **dropdown_defaults)],
    )
)
