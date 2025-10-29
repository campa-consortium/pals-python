from typing import Literal

from .mixin import ThickElement
from .utils import under_construction


@under_construction("ACKicker")
class ACKicker(ThickElement):
    """Time varying kicker element"""

    # Discriminator field
    kind: Literal["ACKicker"] = "ACKicker"

    # Note: ACKickerP parameter group not yet implemented
