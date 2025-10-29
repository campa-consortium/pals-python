from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from .utils import under_construction


@under_construction("Multipole")
class Multipole(ThickElement):
    """Multipole element"""

    # Discriminator field
    kind: Literal["Multipole"] = "Multipole"

    # Multipole-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
