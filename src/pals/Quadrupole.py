from typing import Literal

from .ThickElement import ThickElement
from .MagneticMultipoleParameters import MagneticMultipoleParameters


class Quadrupole(ThickElement):
    """A quadrupole element"""

    # Discriminator field
    kind: Literal["Quadrupole"] = "Quadrupole"

    # Magnetic multipole parameters
    MagneticMultipoleP: MagneticMultipoleParameters
