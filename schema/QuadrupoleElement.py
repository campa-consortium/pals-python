from typing import Literal

from .ThickElement import ThickElement
from .MagneticMultipoleParameters import MagneticMultipoleParameters


class QuadrupoleElement(ThickElement):
    """A quadrupole element"""

    # Discriminator field
    Type: Literal["Quadrupole"] = "Quadrupole"

    # Magnetic multipole parameters
    magnetic_multipole_parameters: MagneticMultipoleParameters
