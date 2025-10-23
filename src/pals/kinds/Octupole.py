from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Octupole")
class Octupole(ThickElement):
    """Octupole element"""

    # Discriminator field
    kind: Literal["Octupole"] = "Octupole"

    # Octupole-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
