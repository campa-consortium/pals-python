from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("Foil")
class Foil(BaseElement):
    """Material that can strip electrons from a particle. Will also cause energy loss and diffusion"""

    # Discriminator field
    kind: Literal["Foil"] = "Foil"
