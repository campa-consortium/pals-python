from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("BeginningEle")
class BeginningEle(BaseElement):
    """Initial element at start of a branch"""

    # Discriminator field
    kind: Literal["BeginningEle"] = "BeginningEle"
