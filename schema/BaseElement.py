from pydantic import (
    BaseModel,
    ConfigDict,
    model_serializer,
)
from typing import Literal, Optional


class BaseElement(BaseModel):
    """A custom base element defining common properties"""

    # Discriminator field
    kind: Literal["BaseElement"] = "BaseElement"

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of BaseElement is created
    model_config = ConfigDict(validate_assignment=True)

    # Unique element name
    name: Optional[str] = None

    @model_serializer
    def _serialize(self):
        data = self.__dict__.copy()
        data.pop("name", None)
        return data
