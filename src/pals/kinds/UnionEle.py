from typing import List, Literal

from .BaseElement import BaseElement


class UnionEle(BaseElement):
    """Union element for overlapping elements"""

    # Discriminator field
    kind: Literal["UnionEle"] = "UnionEle"

    # Elements in the union
    elements: List[BaseElement] = []
