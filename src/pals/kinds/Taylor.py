from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Taylor")
class Taylor(BaseElement):
    """Taylor map element"""

    # Discriminator field
    kind: Literal["Taylor"] = "Taylor"
