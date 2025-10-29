from typing import Literal

from .mixin import ThinElement


class Marker(ThinElement):
    """Zero length element to mark a particular position

    The main purpose of this thin element is to name a position in the beamline.
    """

    # Discriminator field
    kind: Literal["Marker"] = "Marker"
