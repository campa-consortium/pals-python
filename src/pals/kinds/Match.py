from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Match")
class Match(BaseElement):
    """Orbit, Twiss, and dispersion matching element"""

    # Discriminator field
    kind: Literal["Match"] = "Match"
