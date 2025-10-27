from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Foil")
class Foil(BaseElement):
    """Material that can strip electrons from a particle. Will also cause energy loss and diffusion"""

    # Discriminator field
    kind: Literal["Foil"] = "Foil"
