from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters
from ..parameters import MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Kicker")
class Kicker(ThickElement):
    """Particle kicker element"""

    # Discriminator field
    kind: Literal["Kicker"] = "Kicker"

    # Kicker-specific parameters (in addition to inherited ones)
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
