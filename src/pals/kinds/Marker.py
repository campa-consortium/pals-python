from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("Marker")
class Marker(BaseElement):
    """Zero length element to mark a particular position"""

    # Discriminator field
    kind: Literal["Marker"] = "Marker"
