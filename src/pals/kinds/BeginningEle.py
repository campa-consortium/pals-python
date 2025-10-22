from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("BeginningEle")
class BeginningEle(BaseElement):
    """Initial element at start of a branch"""

    # Discriminator field
    kind: Literal["BeginningEle"] = "BeginningEle"
