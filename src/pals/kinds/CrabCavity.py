from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from .utils import under_construction


@under_construction("CrabCavity")
class CrabCavity(ThickElement):
    """RF crab cavity"""

    # Discriminator field
    kind: Literal["CrabCavity"] = "CrabCavity"

    # CrabCavity-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
