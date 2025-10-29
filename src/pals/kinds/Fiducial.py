from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Fiducial")
class Fiducial(BaseElement):
    """Global coordinate system fiducial point"""

    # Discriminator field
    kind: Literal["Fiducial"] = "Fiducial"
