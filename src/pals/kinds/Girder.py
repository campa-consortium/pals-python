from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Girder")
class Girder(BaseElement):
    """Element to support in space a group of other elements"""

    # Discriminator field
    kind: Literal["Girder"] = "Girder"
