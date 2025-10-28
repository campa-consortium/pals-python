from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Sextupole")
class Sextupole(ThickElement):
    """Sextupole element"""

    # Discriminator field
    kind: Literal["Sextupole"] = "Sextupole"

    # Sextupole-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
