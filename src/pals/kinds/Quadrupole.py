from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import MagneticMultipoleParameters, ElectricMultipoleParameters
from ._warnings import under_construction


@under_construction("Quadrupole")
class Quadrupole(ThickElement):
    """Quadrupole element"""

    # Discriminator field
    kind: Literal["Quadrupole"] = "Quadrupole"

    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: MagneticMultipoleParameters
