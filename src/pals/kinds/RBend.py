from typing import Literal, Optional

from .mixin import ThickElement
from ..parameters import (
    BendParameters,
    ElectricMultipoleParameters,
    MagneticMultipoleParameters,
)


class RBend(ThickElement):
    """A rectangular bend element"""

    # Discriminator field
    kind: Literal["RBend"] = "RBend"

    # Bend-specific parameters
    BendP: Optional[BendParameters] = None

    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
