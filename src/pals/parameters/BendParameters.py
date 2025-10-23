from pydantic import BaseModel


class BendParameters(BaseModel):
    """Bend parameters"""

    rho_ref: float = 0.0  # [radian] Reference bend angle
    bend_field_ref: float = 0.0  # [T] Reference bend field
    e1: float = 0.0  # [radian] Entrance end pole face rotation with respect to a sector geometry
    e2: float = 0.0  # [radian] Exit end pole face rotation with respect to a rectangular geometry
    e1_rect: float = 0.0  # [radian] Entrance end pole face rotation with respect to a rectangular geometry
    e2_rect: float = 0.0  # [radian] Exit end pole face rotation with respect to a rectangular geometry
    edge_int1: float = 0.0  # [T*m] Entrance end fringe field integral
    edge_int2: float = 0.0  # [T*m] Exit end fringe field integral
    g_ref: float = 0.0  # [1/m] Reference bend strength = 1/radius_ref
    h1: float = 0.0  # [TODO] Entrance end pole face curvature
    h2: float = 0.0  # [TODO] Exit end pole face curvature
    L_chord: float = 0.0  # [m] Chord length
    L_sagitta: float = 0.0  # [m] Sagitta length (output parameter)
    tilt_ref: float = 0.0  # [radian] Reference tilt
