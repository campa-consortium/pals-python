from typing import Literal, Optional

from .mixin import BaseElement
from ..parameters import FloorShiftParameters


class FloorShift(BaseElement):
    """Global coordinates shift element"""

    # Discriminator field
    kind: Literal["FloorShift"] = "FloorShift"

    # Floor shift-specific parameters
    FloorShiftP: Optional[FloorShiftParameters] = None
