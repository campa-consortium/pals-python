from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from .utils import under_construction


@under_construction("Wiggler")
class Wiggler(ThickElement):
    """Wiggler element"""

    # Discriminator field
    kind: Literal["Wiggler"] = "Wiggler"

    # Wiggler-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
