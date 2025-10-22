from pydantic import BaseModel, ConfigDict


class ReferenceChangeParameters(BaseModel):
    """Reference energy change and/or reference time correction parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    delta_e: float = 0.0  # [eV] Energy change
    delta_pc: float = 0.0  # [momentum*c] Momentum change
    delta_time: float = 0.0  # [s] Time correction
