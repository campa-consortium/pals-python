from typing import Literal

from .ThickElement import ThickElement


class Drift(ThickElement):
    """A field free region"""

    # Discriminator field
    kind: Literal["Drift"] = "Drift"
