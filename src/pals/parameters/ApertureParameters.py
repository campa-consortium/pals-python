from typing import Literal
from pydantic import BaseModel, Field


class ApertureParameters(BaseModel):
    """Aperture parameters"""

    x_limits: list[float | None, float | None] = Field(
        default=[None, None],
        validate_args=lambda x: (x[0] is None or x[1] is None or x[0] < x[1]),
    )
    y_limits: list[float | None, float | None] = Field(
        default=[None, None],
        validate_args=lambda x: (x[0] is None or x[1] is None or x[0] < x[1]),
    )
    shape: Literal["RECTANGULAR", "ELLIPTICAL", "VERTICES", "CUSTOM_SHAPE"] = (
        "RECTANGULAR"
    )
    location: Literal[
        "ENTRANCE_END", "CENTER", "EXIT_END", "BOTH_ENDS", "NOWHERE", "EVERYWHERE"
    ] = "ENTRANCE_END"
    material: str = ""
    thickness: float = Field(default=0.0, ge=0.0)
    aperture_shifts_with_body: bool = False
    aperture_active: bool = True
