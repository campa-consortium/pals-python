from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("Fiducial")
class Fiducial(BaseElement):
    """Global coordinate system fiducial point"""

    # Discriminator field
    kind: Literal["Fiducial"] = "Fiducial"
