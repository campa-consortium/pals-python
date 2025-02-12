from pydantic import BaseModel, ConfigDict
from typing import Optional


class BaseElement(BaseModel):
    """A custom base element defining common properties"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of BaseElement is created
    model_config = ConfigDict(validate_assignment=True)

    # Unique element name
    name: Optional[str] = None
