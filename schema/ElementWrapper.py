from pydantic import BaseModel, Field
from typing import Annotated, Literal, Union
from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement
from schema.DriftElement import DriftElement
from schema.QuadrupoleElement import QuadrupoleElement


class ElementWrapper(BaseModel):
    """Base class for element wrappers"""

    kind: Literal["ElementWrapper"] = "ElementWrapper"

    element: Annotated[
        Union[
            BaseElement,
            ThickElement,
            DriftElement,
            QuadrupoleElement,
        ],
        Field(discriminator="kind"),
    ]

    def to_dict(self):
        element_dict = self.element.model_dump()
        kind = element_dict.pop("kind")
        return {kind: element_dict}

    @classmethod
    def from_dict(cls, data):
        kind = next(iter(data))
        element_data = data[kind]
        element_data["kind"] = kind
        element_class = {
            "Drift": DriftElement,
            "Quadrupole": QuadrupoleElement,
        }[kind]
        element = element_class(**element_data)
        return cls(element=element)
