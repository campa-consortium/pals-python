from pydantic import BaseModel


class RFParameters(BaseModel):
    """RF parameters"""

    frequency: float = 0.0  # [Hz] RF frequency
    harmon: int = 0  # [unitless] RF frequency harmonic number
    voltage: float = 0.0  # [V] RF voltage
    gradient: float = 0.0  # [V/m] RF gradient
    phase: float = 0.0  # [unitless] RF phase in 0 to 2*pi
    multipass_phase: float = 0.0  # [unitless] RF Phase added to multipass elements
    cavity_type: str = "STANDING_WAVE"  # [string] Cavity type
    n_cell: int = 1  # [unitless] Number of cavity cells
