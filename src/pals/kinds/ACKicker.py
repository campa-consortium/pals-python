from typing import Literal

from .ThickElement import ThickElement
from ._warnings import under_construction


@under_construction("ACKicker")
class ACKicker(ThickElement):
    """Time varying kicker element"""

    # Discriminator field
    kind: Literal["ACKicker"] = "ACKicker"

    # Note: ACKickerP parameter group not yet implemented
