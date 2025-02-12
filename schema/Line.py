from pydantic import BaseModel, ConfigDict, Field
from typing import List, Union

from schema.BaseElement import BaseElement


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    # FIXME TypeError: 'list' is not a valid discriminated union variant; should be a `BaseModel` or `dataclass`
    line: List[Union[BaseElement, "Line"]] = Field(..., discriminator="element")
