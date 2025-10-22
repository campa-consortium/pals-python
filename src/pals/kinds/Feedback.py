from typing import Literal

from .BaseElement import BaseElement
from ._warnings import under_construction


@under_construction("Feedback")
class Feedback(BaseElement):
    """Element used to simulate a feedback circuit"""

    # Discriminator field
    kind: Literal["Feedback"] = "Feedback"
