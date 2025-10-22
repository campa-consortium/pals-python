from pydantic import BaseModel, ConfigDict


class SolenoidParameters(BaseModel):
    """Solenoid parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    Ksol: float = 0.0  # Normalized solenoid strength
    Bsol: float = 0.0  # Solenoid field
