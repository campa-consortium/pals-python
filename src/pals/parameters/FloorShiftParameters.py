from pydantic import BaseModel, ConfigDict


class FloorShiftParameters(BaseModel):
    """Floor shift parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    x_offset: float = 0.0
    y_offset: float = 0.0
    z_offset: float = 0.0
    t_offset: float = 0.0
    x_rot: float = 0.0
    y_rot: float = 0.0
    z_rot: float = 0.0
