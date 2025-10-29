from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import (
    RFParameters,
    SolenoidParameters,
    ElectricMultipoleParameters,
    MagneticMultipoleParameters,
)
from .utils import under_construction


@under_construction("RFCavity")
class RFCavity(ThickElement):
    """RF cavity element"""

    # Discriminator field
    kind: Literal["RFCavity"] = "RFCavity"

    # RF-specific parameters
    RFP: Optional[RFParameters] = None
    SolenoidP: Optional[SolenoidParameters] = None

    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
