from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import PatchParameters
from ._warnings import under_construction


@under_construction("Patch")
class Patch(ThickElement):
    """Crooked drift used to shift the reference curve"""

    # Discriminator field
    kind: Literal["Patch"] = "Patch"

    # Patch-specific parameters
    PatchP: Optional[PatchParameters] = None
