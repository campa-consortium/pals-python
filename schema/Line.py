from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, Literal, OrderedDict, Union

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement
from schema.DriftElement import DriftElement
from schema.QuadrupoleElement import QuadrupoleElement


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    kind: Literal["Line"] = "Line"

    line: OrderedDict[
        str,
        Annotated[
            Union[
                BaseElement,
                ThickElement,
                DriftElement,
                QuadrupoleElement,
                "Line",
            ],
            Field(discriminator="kind"),
        ],
    ]


# Avoid circular import issues
Line.model_rebuild()
