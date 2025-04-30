from pydantic import BaseModel, ConfigDict
from typing import List, Literal

from schema.ElementWrapper import ElementWrapper


class Line(BaseModel):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    kind: Literal["Line"] = "Line"

    line: List[ElementWrapper]

    def to_dict(self):
        return {"kind": self.kind, "line": [element.to_dict() for element in self.line]}

    @classmethod
    def from_dict(cls, data):
        line_elements = [ElementWrapper.from_dict(element) for element in data["line"]]
        return cls(line=line_elements)


# Avoid circular import issues
Line.model_rebuild()
