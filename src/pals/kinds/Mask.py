from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Mask")
class Mask(ThickElement):
    """Collimation element"""

    # Discriminator field
    kind: Literal["Mask"] = "Mask"

    # Mask-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
