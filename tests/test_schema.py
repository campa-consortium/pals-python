from pydantic import ValidationError

import json
import yaml

from schema.BaseElement import BaseElement
from schema.ThickElement import ThickElement
from schema.Line import Line


def test_BaseElement():
    # Create one base element with custom name
    element_name = "base_element"
    element = BaseElement(name=element_name)
    assert element.name == element_name


def test_ThickElement():
    # Create one thick element with custom name and length
    element_name = "thick_element"
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


def test_Line():
    # Create first line with one base element
    element1 = BaseElement(name="element1")
    line1 = Line(line=[element1])
    assert line1.line == [element1]
    # Extend first line with one thick element
    element2 = ThickElement(name="element2", length=2.0)
    line1.line.extend(Line(line=[element2]).line)
    assert line1.line == [element1, element2]
    # Create second line with one thick element
    element3 = ThickElement(name="element3", length=3.0)
    line2 = Line(line=[element3])
    # Extend first line with second line
    line1.line.extend(line2.line)
    assert line1.line == [element1, element2, element3]


def test_yaml():
    # Create one base element
    element1 = BaseElement(name="element1")
    # Create one thick element
    element2 = ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = Line(line=[element1, element2])
    # Serialize the Line object to YAML
    yaml_data = yaml.dump(line.model_dump(), default_flow_style=False)
    print(f"\n{yaml_data}")
    # Write the YAML data to a file
    with open("line.yaml", "w") as file:
        file.write(yaml_data)
    # Read the YAML data from the file
    with open("line.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)
    # Parse the YAML data back into a Line object
    loaded_line = Line(**yaml_data)
    assert line == loaded_line


def test_json():
    # Create one base element
    element1 = BaseElement(name="element1")
    # Create one thick element
    element2 = ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = Line(line=[element1, element2])
    # Serialize the Line object to JSON
    json_data = json.dumps(line.model_dump(), sort_keys=True, indent=2)
    print(f"\n{json_data}")
    # Write the JSON data to a file
    with open("line.json", "w") as file:
        file.write(json_data)
    # Read the JSON data from the file
    with open("line.json", "r") as file:
        json_data = json.loads(file.read())
    # Parse the JSON data back into a Line object
    loaded_line = Line(**json_data)
    assert line == loaded_line
