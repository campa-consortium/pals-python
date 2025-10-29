from typing import Literal

from . import BaseElement


class ThinElement(BaseElement):
    """A thin base element with zero segment length"""

    # Discriminator field
    kind: Literal["ThinElement"] = "ThinElement"

    # Segment length in meters (m)
    # always 0 for thin elements, not modifiable
    length: Literal[0.0] = 0.0
