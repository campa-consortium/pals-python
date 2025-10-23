from typing import Literal, Optional

from .BaseElement import BaseElement
from ..parameters import BeamBeamParameters
from ._warnings import under_construction


@under_construction("BeamBeam")
class BeamBeam(BaseElement):
    """Element for simulating colliding beams"""

    # Discriminator field
    kind: Literal["BeamBeam"] = "BeamBeam"

    # Beam-beam-specific parameters
    BeamBeamP: Optional[BeamBeamParameters] = None
