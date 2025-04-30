from typing import Literal

from .ThickElement import ThickElement


class DriftElement(ThickElement):
    """A field free region"""

    # Discriminator field
    Type: Literal["Drift"] = "Drift"
