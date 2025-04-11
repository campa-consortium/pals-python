from typing import Annotated, Literal
from annotated_types import Gt

from .BaseElement import BaseElement


class ThickElement(BaseElement):
    """A thick base element with finite segment length"""

    # Discriminator field
    kind: Literal["ThickElement"] = "ThickElement"

    # Segment length in meters (m)
    length: Annotated[float, Gt(0)]
