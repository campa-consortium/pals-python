from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("Taylor")
class Taylor(BaseElement):
    """Taylor map element"""

    # Discriminator field
    kind: Literal["Taylor"] = "Taylor"
