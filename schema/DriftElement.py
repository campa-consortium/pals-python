from typing import Literal

from .ThickElement import ThickElement


class DriftElement(ThickElement):
    """A field free region"""

    # Discriminator field
    kind: Literal["Drift"] = "Drift"
