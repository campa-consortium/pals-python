from pydantic import BaseModel, ConfigDict


class PatchParameters(BaseModel):
    """Patch parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    x_offset: float = 0.0
    y_offset: float = 0.0
    z_offset: float = 0.0
    x_rot: float = 0.0
    y_rot: float = 0.0
    z_rot: float = 0.0
    flexible: bool = False
    ref_coords: str = "exit_end"  # "entrance_end" or "exit_end"
    user_sets_length: bool = False
