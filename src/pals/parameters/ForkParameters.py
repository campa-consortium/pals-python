from pydantic import BaseModel, ConfigDict


class ForkParameters(BaseModel):
    """Fork parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    to_line: str = ""
    to_ele: str = ""
    direction: str = "FORWARDS"  # "FORWARDS" or "BACKWARDS"
    propagate_reference: bool = True
