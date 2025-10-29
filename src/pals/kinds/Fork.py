from typing import Literal, Optional

from .mixin import BaseElement
from ..parameters import ForkParameters
from .utils import under_construction


@under_construction("Fork")
class Fork(BaseElement):
    """Element used to connect lattice branches together"""

    # Discriminator field
    kind: Literal["Fork"] = "Fork"

    # Fork-specific parameters
    ForkP: Optional[ForkParameters] = None
