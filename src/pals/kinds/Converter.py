from typing import Literal, Optional

from .BaseElement import BaseElement
from ..parameters import ElectricMultipoleParameters, MagneticMultipoleParameters
from ._warnings import under_construction


@under_construction("Converter")
class Converter(BaseElement):
    """Target to produce new species. EG: Positron converter"""

    # Discriminator field
    kind: Literal["Converter"] = "Converter"

    # Converter-specific parameters
    ElectricMultipoleP: Optional[ElectricMultipoleParameters] = None
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None
