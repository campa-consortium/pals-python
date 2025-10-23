from pydantic import BaseModel


class MetaParameters(BaseModel):
    """Meta parameters"""

    alias: str = ""
    ID: str = ""
    label: str = ""
    description: str = ""
