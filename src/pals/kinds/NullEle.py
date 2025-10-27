from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("NullEle")
class NullEle(BaseElement):
    """Placeholder element used for bookkeeping"""

    # Discriminator field
    kind: Literal["NullEle"] = "NullEle"
