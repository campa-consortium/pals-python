from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import (
    BendParameters,
    ElectricMultipoleParameters,
    MagneticMultipoleParameters,
)


class SBend(ThickElement):
    """A sector bend element"""

    # Discriminator field
    kind: Literal["SBend"] = "SBend"

    # Bend-specific parameters
    BendP: Optional[BendParameters] = None

    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
