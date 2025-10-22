from typing import List
from pydantic import BaseModel, ConfigDict


class ApertureParameters(BaseModel):
    """Aperture parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    x_limits: List[float] = [float("nan"), float("nan")]
    y_limits: List[float] = [float("nan"), float("nan")]
    shape: str = "RECTANGULAR"
    location: str = "ENTRANCE_END"
    material: str = ""
    thickness: float = 0.0
    aperture_shifts_with_body: bool = False
    aperture_active: bool = True
