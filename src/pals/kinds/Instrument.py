from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from .utils import under_construction


@under_construction("Instrument")
class Instrument(ThickElement):
    """Measurement element"""

    # Discriminator field
    kind: Literal["Instrument"] = "Instrument"

    # Instrument-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
