from pydantic import BaseModel


class FloorShiftParameters(BaseModel):
    """Floor shift parameters"""

    x_offset: float = 0.0
    y_offset: float = 0.0
    z_offset: float = 0.0
    t_offset: float = 0.0
    x_rot: float = 0.0
    y_rot: float = 0.0
    z_rot: float = 0.0
