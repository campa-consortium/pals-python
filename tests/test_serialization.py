import json
import os
import yaml

import pals


def test_yaml():
    # Create one base element
    element1 = pals.BaseElement(name="element1")
    # Create one thick element
    element2 = pals.ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = pals.BeamLine(name="line", line=[element1, element2])
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
    loaded_line = pals.BeamLine(**yaml_data)
    # Remove the test file
    os.remove(test_file)
    # Validate loaded BeamLine object
    assert line == loaded_line


def test_json():
    # Create one base element
    element1 = pals.BaseElement(name="element1")
    # Create one thick element
    element2 = pals.ThickElement(name="element2", length=2.0)
    # Create line with both elements
    line = pals.BeamLine(name="line", line=[element1, element2])
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
    loaded_line = pals.BeamLine(**json_data)
    # Remove the test file
    os.remove(test_file)
    # Validate loaded BeamLine object
    assert line == loaded_line


def test_comprehensive_lattice():
    """Test a comprehensive lattice using every PALS element at least once"""

    # Create elements in alphabetical order for easy maintenance
    # ACKicker
    ackicker = pals.ACKicker(name="ackicker1", length=0.1)

    # BeamBeam
    beambeam = pals.BeamBeam(name="beambeam1", BeamBeamP=pals.BeamBeamParameters())

    # BeginningEle
    beginning = pals.BeginningEle(name="beginning1")

    # Converter
    converter = pals.Converter(name="converter1")

    # CrabCavity
    crabcavity = pals.CrabCavity(name="crabcavity1", length=0.2)

    # Drift
    drift = pals.Drift(name="drift1", length=0.5)

    # EGun
    egun = pals.EGun(name="egun1", length=0.15)

    # Feedback
    feedback = pals.Feedback(name="feedback1")

    # Fiducial
    fiducial = pals.Fiducial(name="fiducial1")

    # FloorShift
    floorshift = pals.FloorShift(
        name="floorshift1", FloorShiftP=pals.FloorShiftParameters(x_offset=0.1)
    )

    # Foil
    foil = pals.Foil(name="foil1")

    # Fork
    fork = pals.Fork(name="fork1", ForkP=pals.ForkParameters(to_line="line1"))

    # Girder
    girder = pals.Girder(name="girder1")

    # Instrument
    instrument = pals.Instrument(name="instrument1", length=0.05)

    # Kicker
    kicker = pals.Kicker(name="kicker1", length=0.1)

    # Marker
    marker = pals.Marker(name="marker1")

    # Mask
    mask = pals.Mask(name="mask1", length=0.02)

    # Match
    match = pals.Match(name="match1")

    # Multipole
    multipole = pals.Multipole(name="multipole1", length=0.3)

    # NullEle
    nullele = pals.NullEle(name="nullele1")

    # Octupole
    octupole = pals.Octupole(
        name="octupole1",
        length=0.25,
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En3=0.5),
        MetaP=pals.MetaParameters(alias="octupole_test"),
    )

    # Patch
    patch = pals.Patch(
        name="patch1", length=0.4, PatchP=pals.PatchParameters(x_offset=0.05)
    )

    # Quadrupole
    quadrupole = pals.Quadrupole(
        name="quadrupole1",
        length=0.8,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=1.0),
    )

    # RBend
    rbend = pals.RBend(
        name="rbend1",
        length=1.0,
        BendP=pals.BendParameters(rho_ref=2.0),
        ApertureP=pals.ApertureParameters(x_limits=[-0.2, 0.2]),
    )

    # RFCavity
    rfcavity = pals.RFCavity(
        name="rfcavity1",
        length=0.3,
        RFP=pals.RFParameters(frequency=1e9),
        SolenoidP=pals.SolenoidParameters(Ksol=0.05),
    )

    # SBend
    sbend = pals.SBend(
        name="sbend1", length=1.2, BendP=pals.BendParameters(rho_ref=1.5)
    )

    # Sextupole
    sextupole = pals.Sextupole(
        name="sextupole1",
        length=0.2,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn2=1.0),
        ApertureP=pals.ApertureParameters(x_limits=[-0.1, 0.1]),
    )

    # Solenoid
    solenoid = pals.Solenoid(
        name="solenoid1", length=0.6, SolenoidP=pals.SolenoidParameters(Ksol=0.1)
    )

    # Taylor
    taylor = pals.Taylor(name="taylor1")

    # UnionEle
    unionele = pals.UnionEle(name="unionele1", elements=[])

    # Wiggler
    wiggler = pals.Wiggler(name="wiggler1", length=2.0)

    # Create comprehensive lattice
    lattice = pals.BeamLine(
        name="comprehensive_lattice",
        line=[
            beginning,  # Start with beginning element
            fiducial,  # Global coordinate reference
            marker,  # Mark position
            drift,  # Field-free region
            quadrupole,  # Focusing element
            sextupole,  # Chromatic correction
            octupole,  # Higher order correction
            multipole,  # General multipole
            rbend,  # Rectangular bend
            sbend,  # Sector bend
            solenoid,  # Longitudinal focusing
            rfcavity,  # RF acceleration
            crabcavity,  # RF crab cavity
            kicker,  # Transverse kick
            ackicker,  # AC kicker
            patch,  # Coordinate transformation
            floorshift,  # Global coordinate shift
            instrument,  # Measurement device
            mask,  # Collimation
            match,  # Matching element
            egun,  # Electron source
            converter,  # Species conversion
            foil,  # Electron stripping
            beambeam,  # Colliding beams
            feedback,  # Feedback system
            girder,  # Support structure
            fork,  # Branch connection
            taylor,  # Taylor map
            unionele,  # Overlapping elements
            wiggler,  # Undulator
            nullele,  # Placeholder
        ],
    )

    # Test serialization to YAML
    yaml_data = yaml.dump(lattice.model_dump(), default_flow_style=False)
    print(f"\nComprehensive lattice YAML:\n{yaml_data}")

    # Write to temporary file
    yaml_file = "comprehensive_lattice.yaml"
    with open(yaml_file, "w") as file:
        file.write(yaml_data)

    # Read back from file
    with open(yaml_file, "r") as file:
        loaded_yaml_data = yaml.safe_load(file)

    # Deserialize back to Python object using Pydantic model logic
    loaded_lattice = pals.BeamLine(**loaded_yaml_data)

    # Verify the loaded lattice has the correct structure and parameter groups
    assert len(loaded_lattice.line) == 31  # Should have 31 elements

    # Verify specific elements with parameter groups are correctly loaded
    sextupole_loaded = None
    octupole_loaded = None
    rbend_loaded = None
    rfcavity_loaded = None

    for elem in loaded_lattice.line:
        if elem.name == "sextupole1":
            sextupole_loaded = elem
        elif elem.name == "octupole1":
            octupole_loaded = elem
        elif elem.name == "rbend1":
            rbend_loaded = elem
        elif elem.name == "rfcavity1":
            rfcavity_loaded = elem

    # Test that parameter groups are correctly deserialized
    assert sextupole_loaded.MagneticMultipoleP.Bn2 == 1.0
    assert sextupole_loaded.ApertureP.x_limits == [-0.1, 0.1]

    assert octupole_loaded.ElectricMultipoleP.En3 == 0.5
    assert octupole_loaded.MetaP.alias == "octupole_test"

    assert rbend_loaded.BendP.rho_ref == 2.0
    assert rbend_loaded.ApertureP.x_limits == [-0.2, 0.2]

    assert rfcavity_loaded.RFP.frequency == 1e9
    assert rfcavity_loaded.SolenoidP.Ksol == 0.05

    # Test serialization to JSON
    json_data = json.dumps(lattice.model_dump(), sort_keys=True, indent=2)
    print(f"\nComprehensive lattice JSON:\n{json_data}")

    # Write to temporary file
    json_file = "comprehensive_lattice.json"
    with open(json_file, "w") as file:
        file.write(json_data)

    # Read back from file
    with open(json_file, "r") as file:
        loaded_json_data = json.loads(file.read())

    # Deserialize back to Python object using Pydantic model logic
    loaded_lattice_json = pals.BeamLine(**loaded_json_data)

    # Verify the loaded lattice has the correct structure and parameter groups
    assert len(loaded_lattice_json.line) == 31  # Should have 31 elements

    # Verify specific elements with parameter groups are correctly loaded
    sextupole_loaded_json = None
    octupole_loaded_json = None
    rbend_loaded_json = None
    rfcavity_loaded_json = None

    for elem in loaded_lattice_json.line:
        if elem.name == "sextupole1":
            sextupole_loaded_json = elem
        elif elem.name == "octupole1":
            octupole_loaded_json = elem
        elif elem.name == "rbend1":
            rbend_loaded_json = elem
        elif elem.name == "rfcavity1":
            rfcavity_loaded_json = elem

    # Test that parameter groups are correctly deserialized
    assert sextupole_loaded_json.MagneticMultipoleP.Bn2 == 1.0
    assert sextupole_loaded_json.ApertureP.x_limits == [-0.1, 0.1]

    assert octupole_loaded_json.ElectricMultipoleP.En3 == 0.5
    assert octupole_loaded_json.MetaP.alias == "octupole_test"

    assert rbend_loaded_json.BendP.rho_ref == 2.0
    assert rbend_loaded_json.ApertureP.x_limits == [-0.2, 0.2]

    assert rfcavity_loaded_json.RFP.frequency == 1e9
    assert rfcavity_loaded_json.SolenoidP.Ksol == 0.05

    # Clean up temporary files
    os.remove(yaml_file)
    os.remove(json_file)
