from pydantic import BaseModel, ConfigDict


class MetaParameters(BaseModel):
    """Meta parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    alias: str = ""
    ID: str = ""
    label: str = ""
    description: str = ""
