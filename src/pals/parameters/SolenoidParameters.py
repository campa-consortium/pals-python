from pydantic import BaseModel


class SolenoidParameters(BaseModel):
    """Solenoid parameters"""

    Ksol: float = 0.0  # Normalized solenoid strength
    Bsol: float = 0.0  # Solenoid field
