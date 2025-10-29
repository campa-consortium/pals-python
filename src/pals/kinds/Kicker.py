from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from .utils import under_construction


@under_construction("Kicker")
class Kicker(ThickElement):
    """Particle kicker element"""

    # Discriminator field
    kind: Literal["Kicker"] = "Kicker"

    # Kicker-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
