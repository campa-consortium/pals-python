import json
import os
import sys
import yaml

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/")))

from pydantic import ValidationError

from pals_schema.MagneticMultipoleParameters import MagneticMultipoleParameters
from pals_schema.BaseElement import BaseElement
from pals_schema.ThickElement import ThickElement
from pals_schema.DriftElement import DriftElement
from pals_schema.QuadrupoleElement import QuadrupoleElement
from pals_schema.BeamLine import BeamLine


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


def test_DriftElement():
    # Create one drift element with custom name and length
    element_name = "drift_element"
    element_length = 1.0
    element = DriftElement(
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


def test_QuadrupoleElement():
    # Create one drift element with custom name and length
    element_name = "quadrupole_element"
    element_length = 1.0
    element_magnetic_multipole_Bn1 = 1.1
    element_magnetic_multipole_Bn2 = 1.2
    element_magnetic_multipole_Bs1 = 2.1
    element_magnetic_multipole_Bs2 = 2.2
    element_magnetic_multipole_tilt1 = 3.1
    element_magnetic_multipole_tilt2 = 3.2
    element_magnetic_multipole = MagneticMultipoleParameters(
        Bn1=element_magnetic_multipole_Bn1,
        Bs1=element_magnetic_multipole_Bs1,
        tilt1=element_magnetic_multipole_tilt1,
        Bn2=element_magnetic_multipole_Bn2,
        Bs2=element_magnetic_multipole_Bs2,
        tilt2=element_magnetic_multipole_tilt2,
    )
    element = QuadrupoleElement(
        name=element_name,
        length=element_length,
        MagneticMultipoleP=element_magnetic_multipole,
    )
    assert element.name == element_name
    assert element.length == element_length
    assert element.MagneticMultipoleP.Bn1 == element_magnetic_multipole_Bn1
    assert element.MagneticMultipoleP.Bs1 == element_magnetic_multipole_Bs1
    assert element.MagneticMultipoleP.tilt1 == element_magnetic_multipole_tilt1
    assert element.MagneticMultipoleP.Bn2 == element_magnetic_multipole_Bn2
    assert element.MagneticMultipoleP.Bs2 == element_magnetic_multipole_Bs2
    assert element.MagneticMultipoleP.tilt2 == element_magnetic_multipole_tilt2
    # Serialize the BeamLine object to YAML
    yaml_data = yaml.dump(element.model_dump(), default_flow_style=False)
    print(f"\n{yaml_data}")


def test_BeamLine():
    # Create first line with one base element
    element1 = BaseElement(name="element1")
    line1 = BeamLine(line=[element1])
    assert line1.line == [element1]
    # Extend first line with one thick element
    element2 = ThickElement(name="element2", length=2.0)
    line1.line.extend([element2])
    assert line1.line == [element1, element2]
    # Create second line with one drift element
    element3 = DriftElement(name="element3", length=3.0)
    line2 = BeamLine(line=[element3])
    # Extend first line with second line
    line1.line.extend(line2.line)
    assert line1.line == [element1, element2, element3]


def test_yaml():
    # Create one base element
    element1 = BaseElement(name="element1")
    # Create one thick element
    element2 = ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = BeamLine(line=[element1, element2])
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
    line = BeamLine(line=[element1, element2])
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
