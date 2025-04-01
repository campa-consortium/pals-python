from typing import Literal

from .ThickElement import ThickElement
from .MagneticMultipoleParameters import MagneticMultipoleParameters


class QuadrupoleElement(ThickElement):
    """A quadrupole element"""

    # Discriminator field
    element: Literal["QuadrupoleElement"] = "QuadrupoleElement"

    # Magnetic multipole parameters
    MagneticMultipoleP: MagneticMultipoleParameters
