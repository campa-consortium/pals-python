import json
import os
import yaml

from pals import BaseElement
from pals import ThickElement
from pals import BeamLine


def test_yaml():
    # Create one base element
    element1 = BaseElement(name="element1")
    # Create one thick element
    element2 = ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = BeamLine(name="line", line=[element1, element2])
    # Serialize the BeamLine object to YAML
    yaml_data = yaml.dump(line.model_dump(), default_flow_style=False)
    print(f"\n{yaml_data}")
    # Write the YAML data to a test file
    test_file = "line.yaml"
    with open(test_file, "w") as file:
        file.write(yaml_data)
    # Read the YAML data from the test file
    with open(test_file, "r") as file:
        yaml_data = yaml.safe_load(file)
    # Parse the YAML data back into a BeamLine object
    loaded_line = BeamLine(**yaml_data)
    # Remove the test file
    os.remove(test_file)
    # Validate loaded BeamLine object
    assert line == loaded_line


def test_json():
    # Create one base element
    element1 = BaseElement(name="element1")
    # Create one thick element
    element2 = ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = BeamLine(name="line", line=[element1, element2])
    # Serialize the BeamLine object to JSON
    json_data = json.dumps(line.model_dump(), sort_keys=True, indent=2)
    print(f"\n{json_data}")
    # Write the JSON data to a test file
    test_file = "line.json"
    with open(test_file, "w") as file:
        file.write(json_data)
    # Read the JSON data from the test file
    with open(test_file, "r") as file:
        json_data = json.loads(file.read())
    # Parse the JSON data back into a BeamLine object
    loaded_line = BeamLine(**json_data)
    # Remove the test file
    os.remove(test_file)
    # Validate loaded BeamLine object
    assert line == loaded_line
