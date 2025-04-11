from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, Literal, Union

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement
from schema.DriftElement import DriftElement
from schema.QuadrupoleElement import QuadrupoleElement


class Item(BaseModel):
    """An element of a line or a line itself"""

    # Discriminator field
    element: Literal["Item"] = "Item"

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    # NOTE Since pydantic 2.9, the discriminator must be applied to the union type, not the list
    #      (see https://github.com/pydantic/pydantic/issues/10352)
    item: Annotated[
        Union[
            BaseElement,
            ThickElement,
            DriftElement,
            QuadrupoleElement,
        ],
        Field(discriminator="element"),
    ]
