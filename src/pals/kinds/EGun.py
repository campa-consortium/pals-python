from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("EGun")
class EGun(ThickElement):
    """Electron gun"""

    # Discriminator field
    kind: Literal["EGun"] = "EGun"

    # EGun-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
