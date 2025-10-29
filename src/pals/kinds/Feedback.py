from typing import Literal

from .mixin import BaseElement
from .utils import under_construction


@under_construction("Feedback")
class Feedback(BaseElement):
    """Element used to simulate a feedback circuit"""

    # Discriminator field
    kind: Literal["Feedback"] = "Feedback"
