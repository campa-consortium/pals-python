from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import ElectricMultipoleParameters
from ..parameters import MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Wiggler")
class Wiggler(ThickElement):
    """Wiggler element"""

    # Discriminator field
    kind: Literal["Wiggler"] = "Wiggler"

    # Wiggler-specific parameters (in addition to inherited ones)
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
