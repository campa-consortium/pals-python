from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters
from ..parameters import MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("EGun")
class EGun(ThickElement):
    """Electron gun"""

    # Discriminator field
    kind: Literal["EGun"] = "EGun"

    # EGun-specific parameters (in addition to inherited ones)
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
