from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("NullEle")
class NullEle(BaseElement):
    """Placeholder element used for bookkeeping"""

    # Discriminator field
    kind: Literal["NullEle"] = "NullEle"
