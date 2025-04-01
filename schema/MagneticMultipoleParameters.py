from pydantic import BaseModel, ConfigDict


class MagneticMultipoleParameters(BaseModel):
    """Magnetic multipole parameters"""

    # Validate every time a new value is assigned to an attribute,
    # not only when an instance of MagneticMultipoleP is created
    model_config = ConfigDict(validate_assignment=True)

    # Tilt
    tilt: float
