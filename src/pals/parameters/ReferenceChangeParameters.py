from pydantic import BaseModel


class ReferenceChangeParameters(BaseModel):
    """Reference energy change and/or reference time correction parameters"""

    dE_ref: float = 0.0  # Change in reference energy
    extra_dtime_ref: float = 0.0  # Reference time deviation from nominal
