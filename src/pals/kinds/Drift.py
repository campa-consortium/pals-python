from typing import Literal

from .ThickElement import ThickElement


class Drift(ThickElement):
    """Field free region"""

    # Discriminator field
    kind: Literal["Drift"] = "Drift"
