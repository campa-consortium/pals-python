from pydantic import ConfigDict, Field, model_validator
from typing import Annotated, List, Literal, Union

from pals.BaseElement import BaseElement
from pals.ThickElement import ThickElement
from pals.Drift import Drift
from pals.Quadrupole import Quadrupole


class BeamLine(BaseElement):
    """A line of elements and/or other lines"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of BeamLine is created
    model_config = ConfigDict(validate_assignment=True)

    kind: Literal["BeamLine"] = "BeamLine"

    line: List[
        Annotated[
            Union[
                BaseElement,
                ThickElement,
                Drift,
                Quadrupole,
                "BeamLine",
            ],
            Field(discriminator="kind"),
        ]
    ]

    @model_validator(mode="before")
    @classmethod
    def unpack_yaml_structure(cls, data):
        # Handle the top-level one-key dict: unpack the line's name
        if isinstance(data, dict) and len(data) == 1:
            name, value = list(data.items())[0]
            if not isinstance(value, dict):
                raise TypeError(
                    f"Value for line key {name!r} must be a dict, but we got {value!r}"
                )
            value["name"] = name
            data = value
        # Handle the 'line' field: unpack each element's name
        if "line" not in data:
            raise ValueError("'line' field is missing")
        if not isinstance(data["line"], list):
            raise TypeError("'line' must be a list")
        new_line = []
        # Loop over all elements in the line
        for item in data["line"]:
            # An element can be a string that refers to another element
            if isinstance(item, str):
                raise RuntimeError("Reference/alias elements not yet implemented")
            # An element can be a dict
            elif isinstance(item, dict):
                if not (len(item) == 1):
                    raise ValueError(
                        f"Each element must be a dict with exactly one key (the element's name), but we got {item!r}"
                    )
                name, fields = list(item.items())[0]
                if not isinstance(fields, dict):
                    raise TypeError(
                        f"Value for element key {name!r} must be a dict (the element's properties), but we got {fields!r}"
                    )
                fields["name"] = name
                new_line.append(fields)
            # An element can be an instance of an existing model
            elif isinstance(item, BaseElement):
                # Nothing to do, keep the element as is
                new_line.append(item)
            else:
                raise TypeError(
                    f"Value for element key {name!r} must be a reference string or a dict, but we got {item!r}"
                )
        data["line"] = new_line
        return data

    def model_dump(self, *args, **kwargs):
        """This makes sure the element name property is moved out and up to a one-key dictionary"""
        # Use base element dump first and return a dict {key: value}, where 'key'
        # is the name of the line and 'value' is a dict with all other properties
        data = super().model_dump(*args, **kwargs)
        # Reformat 'line' field as list of element dicts
        new_line = []
        for elem in self.line:
            # Use custom dump for each line element, which now returns a dict
            elem_dict = elem.model_dump(**kwargs)
            new_line.append(elem_dict)
        data[self.name]["line"] = new_line
        return data


# Avoid circular import issues
BeamLine.model_rebuild()
