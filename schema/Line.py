from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, List, Literal, Union

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    # NOTE Since pydantic 2.9, the discriminator must be applied to the union type, not the list
    #      (see https://github.com/pydantic/pydantic/issues/10352)
    line: List[
        Annotated[
            Union[BaseElement, ThickElement, "Line"], Field(discriminator="element")
        ]
    ]

    # Discriminator field
    element: Literal["Line"] = "Line"


# Avoid circular import issues
Line.model_rebuild()
