from typing import Literal

from .mixin import ThickElement


class Drift(ThickElement):
    """Field free region"""

    # Discriminator field
    kind: Literal["Drift"] = "Drift"
