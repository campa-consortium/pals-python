from pydantic import BaseModel


class ForkParameters(BaseModel):
    """Fork parameters"""

    to_line: str = ""
    to_ele: str = ""
    direction: str = "FORWARDS"  # "FORWARDS" or "BACKWARDS"
    propagate_reference: bool = True
