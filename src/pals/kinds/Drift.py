from typing import Literal

from .ThickElement import ThickElement
from ._warnings import under_construction


@under_construction("Drift")
class Drift(ThickElement):
    """Field free region"""

    # Discriminator field
    kind: Literal["Drift"] = "Drift"
