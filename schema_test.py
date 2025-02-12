from schema import BaseElement


def test_BaseElement():
    element_name = "my_element"
    element = BaseElement(name=element_name)
    assert element.name == element_name
