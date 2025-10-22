from pydantic import BaseModel, ConfigDict


class ReferenceParameters(BaseModel):
    """Reference parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    species_ref: str = ""
    pc_ref: float = 0.0  # [momentum*c] Reference momentum times speed of light
    E_tot_ref: float = 0.0  # [eV] Reference total energy
    time_ref: float = 0.0  # [s] Reference time
    location: str = ""  # Where reference parameters are evaluated
