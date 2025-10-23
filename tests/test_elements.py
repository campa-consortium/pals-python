from pydantic import ValidationError

import pals


def test_BaseElement():
    # Create one base element with custom name
    element_name = "base_element"
    element = pals.BaseElement(name=element_name)
    assert element.name == element_name


def test_ThickElement():
    # Create one thick element with custom name and length
    element_name = "thick_element"
    element_length = 1.0
    element = pals.ThickElement(
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
    element = pals.Drift(
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
    element_magnetic_multipole = pals.MagneticMultipoleParameters(
        Bn1=element_magnetic_multipole_Bn1,
        Bs1=element_magnetic_multipole_Bs1,
        tilt1=element_magnetic_multipole_tilt1,
        Bn2=element_magnetic_multipole_Bn2,
        Bs2=element_magnetic_multipole_Bs2,
        tilt2=element_magnetic_multipole_tilt2,
    )
    element = pals.Quadrupole(
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
    element1 = pals.BaseElement(name="element1")
    line1 = pals.BeamLine(name="line1", line=[element1])
    assert line1.line == [element1]
    # Extend first line with one thick element
    element2 = pals.ThickElement(name="element2", length=2.0)
    line1.line.extend([element2])
    assert line1.line == [element1, element2]
    # Create second line with one drift element
    element3 = pals.Drift(name="element3", length=3.0)
    line2 = pals.BeamLine(name="line2", line=[element3])
    # Extend first line with second line
    line1.line.extend(line2.line)
    assert line1.line == [element1, element2, element3]


def test_Marker():
    """Test Marker element"""
    element = pals.Marker(name="marker1")
    assert element.name == "marker1"
    assert element.kind == "Marker"


def test_Sextupole():
    """Test Sextupole element"""
    element = pals.Sextupole(
        name="sext1",
        length=0.5,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn2=1.0),
        ApertureP=pals.ApertureParameters(x_limits=[-0.1, 0.1]),
    )
    assert element.name == "sext1"
    assert element.length == 0.5
    assert element.kind == "Sextupole"
    assert element.MagneticMultipoleP.Bn2 == 1.0
    assert element.ApertureP.x_limits == [-0.1, 0.1]


def test_Octupole():
    """Test Octupole element"""
    element = pals.Octupole(
        name="oct1",
        length=0.3,
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En3=0.5),
        MetaP=pals.MetaParameters(alias="octupole_test"),
    )
    assert element.name == "oct1"
    assert element.length == 0.3
    assert element.kind == "Octupole"
    assert element.ElectricMultipoleP.En3 == 0.5
    assert element.MetaP.alias == "octupole_test"


def test_Multipole():
    """Test Multipole element"""
    element = pals.Multipole(
        name="mult1",
        length=0.4,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=2.0, Bn2=1.5),
        BodyShiftP=pals.BodyShiftParameters(x_offset=0.01),
    )
    assert element.name == "mult1"
    assert element.length == 0.4
    assert element.kind == "Multipole"
    assert element.MagneticMultipoleP.Bn1 == 2.0
    assert element.BodyShiftP.x_offset == 0.01


def test_RBend():
    """Test RBend element"""
    bend_params = pals.BendParameters(rho_ref=1.0, bend_field_ref=2.0)
    element = pals.RBend(
        name="rbend1",
        length=1.0,
        BendP=bend_params,
        ApertureP=pals.ApertureParameters(x_limits=[-0.2, 0.2]),
        MetaP=pals.MetaParameters(description="Test bend"),
    )
    assert element.name == "rbend1"
    assert element.length == 1.0
    assert element.kind == "RBend"
    assert element.BendP.rho_ref == 1.0
    assert element.ApertureP.x_limits == [-0.2, 0.2]
    assert element.MetaP.description == "Test bend"


def test_SBend():
    """Test SBend element"""
    bend_params = pals.BendParameters(rho_ref=1.5, bend_field_ref=3.0)
    element = pals.SBend(
        name="sbend1",
        length=1.2,
        BendP=bend_params,
        ReferenceP=pals.ReferenceParameters(species_ref="proton"),
    )
    assert element.name == "sbend1"
    assert element.length == 1.2
    assert element.kind == "SBend"
    assert element.BendP.rho_ref == 1.5
    assert element.ReferenceP.species_ref == "proton"


def test_Solenoid():
    """Test Solenoid element"""
    sol_params = pals.SolenoidParameters(Ksol=0.1, Bsol=0.2)
    element = pals.Solenoid(
        name="sol1",
        length=0.8,
        SolenoidP=sol_params,
    )
    assert element.name == "sol1"
    assert element.length == 0.8
    assert element.kind == "Solenoid"
    assert element.SolenoidP.Ksol == 0.1


def test_RFCavity():
    """Test RFCavity element"""
    rf_params = pals.RFParameters(frequency=1e9, voltage=1e6)
    element = pals.RFCavity(
        name="rf1",
        length=0.5,
        RFP=rf_params,
        SolenoidP=pals.SolenoidParameters(Ksol=0.05),
    )
    assert element.name == "rf1"
    assert element.length == 0.5
    assert element.kind == "RFCavity"
    assert element.RFP.frequency == 1e9
    assert element.SolenoidP.Ksol == 0.05


def test_Patch():
    """Test Patch element"""
    patch_params = pals.PatchParameters(x_offset=0.1, y_offset=0.2)
    element = pals.Patch(
        name="patch1",
        length=0.3,
        PatchP=patch_params,
        ReferenceChangeP=pals.ReferenceChangeParameters(dE_ref=1e6),
    )
    assert element.name == "patch1"
    assert element.length == 0.3
    assert element.kind == "Patch"
    assert element.PatchP.x_offset == 0.1
    assert element.ReferenceChangeP.dE_ref == 1e6


def test_FloorShift():
    """Test FloorShift element"""
    floor_params = pals.FloorShiftParameters(x_offset=0.5, z_offset=1.0)
    element = pals.FloorShift(
        name="floor1",
        FloorShiftP=floor_params,
        MetaP=pals.MetaParameters(alias="floor_test"),
    )
    assert element.name == "floor1"
    assert element.kind == "FloorShift"
    assert element.FloorShiftP.x_offset == 0.5
    assert element.MetaP.alias == "floor_test"


def test_Fork():
    """Test Fork element"""
    fork_params = pals.ForkParameters(to_line="line1", direction="FORWARDS")
    element = pals.Fork(
        name="fork1",
        ForkP=fork_params,
        ReferenceP=pals.ReferenceParameters(species_ref="electron"),
    )
    assert element.name == "fork1"
    assert element.kind == "Fork"
    assert element.ForkP.to_line == "line1"
    assert element.ReferenceP.species_ref == "electron"


def test_BeamBeam():
    """Test BeamBeam element"""
    bb_params = pals.BeamBeamParameters()
    element = pals.BeamBeam(
        name="bb1",
        BeamBeamP=bb_params,
        ApertureP=pals.ApertureParameters(x_limits=[-0.05, 0.05]),
    )
    assert element.name == "bb1"
    assert element.kind == "BeamBeam"
    assert element.ApertureP.x_limits == [-0.05, 0.05]


def test_BeginningEle():
    """Test BeginningEle element"""
    element = pals.BeginningEle(
        name="begin1", MetaP=pals.MetaParameters(description="Start of lattice")
    )
    assert element.name == "begin1"
    assert element.kind == "BeginningEle"
    assert element.MetaP.description == "Start of lattice"


def test_Fiducial():
    """Test Fiducial element"""
    element = pals.Fiducial(
        name="fid1", ReferenceP=pals.ReferenceParameters(species_ref="proton")
    )
    assert element.name == "fid1"
    assert element.kind == "Fiducial"
    assert element.ReferenceP.species_ref == "proton"


def test_NullEle():
    """Test NullEle element"""
    element = pals.NullEle(name="null1")
    assert element.name == "null1"
    assert element.kind == "NullEle"


def test_Kicker():
    """Test Kicker element"""
    element = pals.Kicker(
        name="kick1",
        length=0.2,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.5),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.3),
    )
    assert element.name == "kick1"
    assert element.length == 0.2
    assert element.kind == "Kicker"
    assert element.MagneticMultipoleP.Bn1 == 0.5
    assert element.ElectricMultipoleP.En1 == 0.3


def test_ACKicker():
    """Test ACKicker element"""
    element = pals.ACKicker(name="ackick1", length=0.15)
    assert element.name == "ackick1"
    assert element.length == 0.15
    assert element.kind == "ACKicker"


def test_CrabCavity():
    """Test CrabCavity element"""
    element = pals.CrabCavity(
        name="crab1",
        length=0.25,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.8),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.4),
    )
    assert element.name == "crab1"
    assert element.length == 0.25
    assert element.kind == "CrabCavity"
    assert element.MagneticMultipoleP.Bn1 == 0.8
    assert element.ElectricMultipoleP.En1 == 0.4


def test_EGun():
    """Test EGun element"""
    element = pals.EGun(
        name="egun1",
        length=0.1,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=1.2),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.6),
    )
    assert element.name == "egun1"
    assert element.length == 0.1
    assert element.kind == "EGun"
    assert element.MagneticMultipoleP.Bn1 == 1.2
    assert element.ElectricMultipoleP.En1 == 0.6


def test_Feedback():
    """Test Feedback element"""
    element = pals.Feedback(
        name="fb1", MetaP=pals.MetaParameters(alias="feedback_test")
    )
    assert element.name == "fb1"
    assert element.kind == "Feedback"
    assert element.MetaP.alias == "feedback_test"


def test_Girder():
    """Test Girder element"""
    element = pals.Girder(name="girder1")
    assert element.name == "girder1"
    assert element.kind == "Girder"


def test_Instrument():
    """Test Instrument element"""
    element = pals.Instrument(
        name="inst1",
        length=0.05,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.2),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.1),
    )
    assert element.name == "inst1"
    assert element.length == 0.05
    assert element.kind == "Instrument"
    assert element.MagneticMultipoleP.Bn1 == 0.2
    assert element.ElectricMultipoleP.En1 == 0.1


def test_Mask():
    """Test Mask element"""
    element = pals.Mask(
        name="mask1",
        length=0.02,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.15),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.08),
    )
    assert element.name == "mask1"
    assert element.length == 0.02
    assert element.kind == "Mask"
    assert element.MagneticMultipoleP.Bn1 == 0.15
    assert element.ElectricMultipoleP.En1 == 0.08


def test_Match():
    """Test Match element"""
    element = pals.Match(
        name="match1", BodyShiftP=pals.BodyShiftParameters(x_offset=0.01, y_rot=0.02)
    )
    assert element.name == "match1"
    assert element.kind == "Match"
    assert element.BodyShiftP.x_offset == 0.01
    assert element.BodyShiftP.y_rot == 0.02


def test_Taylor():
    """Test Taylor element"""
    element = pals.Taylor(
        name="taylor1",
        ReferenceChangeP=pals.ReferenceChangeParameters(
            dE_ref=1e6, extra_dtime_ref=1e-9
        ),
    )
    assert element.name == "taylor1"
    assert element.kind == "Taylor"
    assert element.ReferenceChangeP.dE_ref == 1e6
    assert element.ReferenceChangeP.extra_dtime_ref == 1e-9


def test_Wiggler():
    """Test Wiggler element"""
    element = pals.Wiggler(
        name="wig1",
        length=2.0,
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.5),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.3),
    )
    assert element.name == "wig1"
    assert element.length == 2.0
    assert element.kind == "Wiggler"
    assert element.MagneticMultipoleP.Bn1 == 0.5
    assert element.ElectricMultipoleP.En1 == 0.3


def test_Converter():
    """Test Converter element"""
    element = pals.Converter(
        name="conv1",
        MagneticMultipoleP=pals.MagneticMultipoleParameters(Bn1=0.4),
        ElectricMultipoleP=pals.ElectricMultipoleParameters(En1=0.2),
    )
    assert element.name == "conv1"
    assert element.kind == "Converter"
    assert element.MagneticMultipoleP.Bn1 == 0.4
    assert element.ElectricMultipoleP.En1 == 0.2


def test_Foil():
    """Test Foil element"""
    element = pals.Foil(name="foil1")
    assert element.name == "foil1"
    assert element.kind == "Foil"


def test_UnionEle():
    """Test UnionEle element"""
    element = pals.UnionEle(name="union1", elements=[])
    assert element.name == "union1"
    assert element.kind == "UnionEle"
    assert element.elements == []
