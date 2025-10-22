from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters
from ..parameters import MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("CrabCavity")
class CrabCavity(ThickElement):
    """RF crab cavity"""

    # Discriminator field
    kind: Literal["CrabCavity"] = "CrabCavity"

    # CrabCavity-specific parameters (in addition to inherited ones)
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
