from pals import MagneticMultipoleParameters

# Import parameter classes
from pals.parameters import (
    SolenoidParameters,
    FloorParameters,
    TrackingParameters,
    FloorShiftParameters,
    BeamBeamParameters,
    ApertureParameters,
    ElectricMultipoleParameters,
    ReferenceParameters,
    BodyShiftParameters,
    ReferenceChangeParameters,
    PatchParameters,
    MetaParameters,
    ForkParameters,
    RFParameters,
    BendParameters,
)


def test_ParameterClasses():
    """Test parameter classes"""
    # Test ApertureParameters
    aperture = ApertureParameters(x_limits=[-0.1, 0.1], y_limits=[-0.05, 0.05])
    assert aperture.x_limits == [-0.1, 0.1]

    # Test BodyShiftParameters
    body_shift = BodyShiftParameters(x_offset=0.01, y_rot=0.02)
    assert body_shift.x_offset == 0.01

    # Test MetaParameters
    meta = MetaParameters(alias="test", description="test element")
    assert meta.alias == "test"

    # Test ElectricMultipoleParameters
    emp = ElectricMultipoleParameters(En1=1.0, Es1=0.5)
    assert emp.En1 == 1.0

    # Test MagneticMultipoleParameters
    mmp = MagneticMultipoleParameters(Bn1=1.0, Bs1=0.5)
    assert mmp.Bn1 == 1.0
    assert mmp.Bs1 == 0.5

    # Test SolenoidParameters
    sol = SolenoidParameters(Ksol=0.1, Bsol=0.2)
    assert sol.Ksol == 0.1

    # Test RFParameters
    rf = RFParameters(frequency=1e9, voltage=1e6)
    assert rf.frequency == 1e9

    # Test BendParameters
    bend = BendParameters(rho_ref=1.0, bend_field_ref=2.0)
    assert bend.rho_ref == 1.0

    # Test PatchParameters
    patch = PatchParameters(x_offset=0.1, flexible=True)
    assert patch.x_offset == 0.1

    # Test FloorShiftParameters
    floor = FloorShiftParameters(x_offset=0.5, z_offset=1.0)
    assert floor.x_offset == 0.5

    # Test ForkParameters
    fork = ForkParameters(to_line="line1", direction="FORWARDS")
    assert fork.to_line == "line1"

    # Test ReferenceParameters
    ref = ReferenceParameters(species_ref="electron", pc_ref=1e6)
    assert ref.species_ref == "electron"

    # Test TrackingParameters
    tracking = TrackingParameters(is_on=True)
    assert tracking.is_on

    # Test FloorParameters
    floor_pos = FloorParameters(x_offset=0.1, y_offset=0.2, z_offset=0.3)
    assert floor_pos.x_offset == 0.1
    assert floor_pos.y_offset == 0.2
    assert floor_pos.z_offset == 0.3

    # Test ReferenceChangeParameters
    ref_change = ReferenceChangeParameters(pc_change=1e6, t_change=1e-9)
    assert ref_change.pc_change == 1e6
    assert ref_change.t_change == 1e-9

    # Test BeamBeamParameters
    beambeam = BeamBeamParameters()
    assert beambeam is not None
