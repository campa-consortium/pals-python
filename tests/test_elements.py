from pydantic import ValidationError

from pals import MagneticMultipoleParameters
from pals import BaseElement
from pals import ThickElement
from pals import Drift
from pals import Quadrupole
from pals import BeamLine


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


def test_Drift():
    # Create one drift element with custom name and length
    element_name = "drift_element"
    element_length = 1.0
    element = Drift(
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


def test_Quadrupole():
    import yaml

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
    element = Quadrupole(
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
    line1 = BeamLine(name="line1", line=[element1])
    assert line1.line == [element1]
    # Extend first line with one thick element
    element2 = ThickElement(name="element2", length=2.0)
    line1.line.extend([element2])
    assert line1.line == [element1, element2]
    # Create second line with one drift element
    element3 = Drift(name="element3", length=3.0)
    line2 = BeamLine(name="line2", line=[element3])
    # Extend first line with second line
    line1.line.extend(line2.line)
    assert line1.line == [element1, element2, element3]
