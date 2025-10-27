from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import (
    SolenoidParameters,
    ElectricMultipoleParameters,
    MagneticMultipoleParameters,
)
from .utils import under_construction


@under_construction("Solenoid")
class Solenoid(ThickElement):
    """Solenoid element"""

    # Discriminator field
    kind: Literal["Solenoid"] = "Solenoid"

    # Solenoid-specific parameters
    SolenoidP: Optional[SolenoidParameters] = None

    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
