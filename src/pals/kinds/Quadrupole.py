from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import MagneticMultipoleParameters, ElectricMultipoleParameters


class Quadrupole(ThickElement):
    """Quadrupole element"""

    # Discriminator field
    kind: Literal["Quadrupole"] = "Quadrupole"

    # Octupole-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: MagneticMultipoleParameters
