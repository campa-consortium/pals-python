from typing import Annotated, Literal
from annotated_types import Gt

from .BaseElement import BaseElement


class ThickElement(BaseElement):
    """A thick base element with finite segment length"""

    # Segment length in meters (m)
    Length: Annotated[float, Gt(0)]

    # Discriminator field
    element: Literal["ThickElement"] = "ThickElement"
