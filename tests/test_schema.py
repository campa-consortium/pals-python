from pydantic import ValidationError

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement


def test_BaseElement():
    # Create base element with custom name
    element_name = "my_base_element"
    element = BaseElement(name=element_name)
    assert element.name == element_name


def test_ThickElement():
    # Create thick element with custom name and length
    element_name = "my_thick_element"
    element_length = 1.0
    element = ThickElement(
        name=element_name,
        length=element_length,
    )
    assert element.name == element_name
    assert element.length == element_length
    # Try to assign negative length and
    # detect validation error without breaking pytest
    element_length = -1.0
    passed = True
    try:
        element.length = element_length
    except ValidationError as e:
        print(e)
        passed = False
    assert not passed
