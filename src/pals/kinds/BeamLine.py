from pydantic import model_validator
from typing import List, Literal

from .all_elements import get_all_elements_as_annotation
from .mixin import BaseElement


class BeamLine(BaseElement):
    """A line of elements and/or other lines"""

    kind: Literal["BeamLine"] = "BeamLine"

    line: List[get_all_elements_as_annotation()]

    @model_validator(mode="before")
    @classmethod
    def unpack_yaml_structure(cls, data):
        """Unpack YAML/JSON/...-like structure for BeamLine elements"""
        from pals.kinds.mixin.all_element_mixin import unpack_element_list_structure

        return unpack_element_list_structure(data, "line", "line")

    def model_dump(self, *args, **kwargs):
        """Custom model dump for BeamLine to handle element list formatting"""
        from pals.kinds.mixin.all_element_mixin import dump_element_list

        return dump_element_list(self, "line", *args, **kwargs)
