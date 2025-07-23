from pydantic import ConfigDict, Field, model_validator
from typing import Annotated, List, Literal, Union

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement
from schema.DriftElement import DriftElement
from schema.QuadrupoleElement import QuadrupoleElement


class Line(BaseElement):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of Line is created
    model_config = ConfigDict(validate_assignment=True)

    kind: Literal["Line"] = "Line"

    line: List[
        Annotated[
            Union[
                BaseElement,
                ThickElement,
                DriftElement,
                QuadrupoleElement,
                "Line",
            ],
            Field(discriminator="kind"),
        ]
    ]

    # @field_validator("line", mode="before")
    # @classmethod
    # def parse_list_of_dicts(cls, value):
    #    """This method inserts the key of the one-key dictionary into
    #    the name attribute of the elements"""
    #    if not isinstance(value, list):
    #        raise TypeError("line must be a list")

    #    if value and isinstance(value[0], BaseModel):
    #        # Already a list of models; nothing to do
    #        return value

    #    # we expect a list of dicts or strings
    #    elements = []
    #    for item_dict in value:
    #        # an element is either a reference string to another element or a dict
    #        if isinstance(item_dict, str):
    #            raise RuntimeError("Reference/alias elements not yet implemented")

    #        elif isinstance(item_dict, dict):
    #            if not (isinstance(item_dict, dict) and len(item_dict) == 1):
    #                raise ValueError(
    #                    f"Each line element must be a dict with exactly one key, the name of the element, but we got: {item_dict!r}"
    #                )
    #            [(name, fields)] = item_dict.items()

    #            if not isinstance(fields, dict):
    #                raise ValueError(
    #                    f"Value for element key '{name}' must be a dict (got {fields!r})"
    #                )

    #        # Insert the name into the fields dict
    #        fields["name"] = name
    #        elements.append(fields)
    #    return elements

    @model_validator(mode="before")
    @classmethod
    def unpack_yaml_structure(cls, data):
        # Handle the top-level dict
        if isinstance(data, dict) and len(data) == 1:
            name, value = list(data.items())[0]
            value = dict(value)
            value["name"] = name
            data = value
        # Now handle the 'line' field if present: unpack each element's name
        if "line" in data and isinstance(data["line"], list):
            new_line = []
            for item in data["line"]:
                if isinstance(item, dict) and len(item) == 1:
                    elem_name, elem_fields = list(item.items())[0]
                    elem_fields = dict(elem_fields)
                    elem_fields["name"] = elem_name
                    new_line.append(elem_fields)
                else:
                    new_line.append(item)
            data["line"] = new_line
        return data

    def model_dump(self, *args, **kwargs):
        """This makes sure the element name property is moved out and up to a one-key dictionary"""
        # Use base element dump first and return a one-element list of the form
        # [{key: value}], where 'key' is the name of the line and 'value' is a
        # dict with all other properties
        data = super().model_dump(*args, **kwargs)
        # Reformat 'line' field as list of single-key dicts
        new_line = []
        for elem in self.line:
            #  Use custom dump for each line element
            elem_dict = elem.model_dump(**kwargs)[0]
            new_line.append(elem_dict)
        data[0][self.name]["line"] = new_line
        return data


# Avoid circular import issues
Line.model_rebuild()
