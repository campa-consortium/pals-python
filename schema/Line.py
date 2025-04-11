from pydantic import BaseModel, ConfigDict
from typing import List


from schema.Item import Item


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    line: List[Item]


# Avoid circular import issues
Line.model_rebuild()
