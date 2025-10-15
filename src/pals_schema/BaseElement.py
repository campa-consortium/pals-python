from pydantic import BaseModel, ConfigDict
from typing import Literal


class BaseElement(BaseModel):
    """A custom base element defining common properties"""

    # Discriminator field
    kind: Literal["BaseElement"] = "BaseElement"

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of BaseElement is created
    model_config = ConfigDict(validate_assignment=True)

    # element name
    name: str

    def model_dump(self, *args, **kwargs):
        """This makes sure the element name property is moved out and up to a one-key dictionary"""
        elem_dict = super().model_dump(*args, **kwargs)
        name = elem_dict.pop("name", None)
        if name is None:
            raise ValueError("Element missing 'name' attribute")
        # Return a dict {name: properties} rather than a single-item list
        # This makes the serialized form a plain dict so it can be passed to
        # constructors using keyword expansion (e.g., Model(**data))
        data = {name: elem_dict}
        return data
