from pydantic import BaseModel, ConfigDict


class FloorParameters(BaseModel):
    """Floor position and orientation parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    x_position: float = 0.0  # [m] Floor position in x
    y_position: float = 0.0  # [m] Floor position in y
    z_position: float = 0.0  # [m] Floor position in z
    x_rotation: float = 0.0  # [radian] Floor rotation around x
    y_rotation: float = 0.0  # [radian] Floor rotation around y
    z_rotation: float = 0.0  # [radian] Floor rotation around z
