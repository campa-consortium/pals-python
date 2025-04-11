from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, List, Literal


from schema.Item import Item


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Discriminator field
    element: Literal["Line"] = "Line"

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    line: List[Annotated[Item, Field(discriminator="element")]]


# Avoid circular import issues
Line.model_rebuild()
