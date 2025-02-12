from typing import Annotated
from annotated_types import Gt

from .BaseElement import BaseElement


class ThickElement(BaseElement):
    """A thick base element with finite segment length"""

    # Segment length in meters (m)
    length: Annotated[float, Gt(0)]
