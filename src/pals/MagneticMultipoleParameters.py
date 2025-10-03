from pydantic import BaseModel, ConfigDict, model_validator
from typing import Any, Dict


class MagneticMultipoleParameters(BaseModel):
    """Magnetic multipole parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    # Custom validation of magnetic multipole order
    def _validate_order(key_num, msg):
        if key_num.isdigit():
            if key_num.startswith("0") and key_num != "0":
                raise ValueError(msg)
        else:
            raise ValueError(msg)

    # Custom validation to be applied before standard validation
    @model_validator(mode="before")
    def validate(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        # loop over all attributes
        for key in values:
            # validate tilt parameters 'tiltN'
            if key.startswith("tilt"):
                key_num = key[4:]
                msg = " ".join(
                    [
                        f"Invalid tilt parameter: '{key}'.",
                        "Tilt parameter must be of the form 'tiltN', where 'N' is an integer.",
                    ]
                )
                cls._validate_order(key_num, msg)
            # validate normal component parameters 'BnN'
            elif key.startswith("Bn"):
                key_num = key[2:]
                msg = " ".join(
                    [
                        f"Invalid normal component parameter: '{key}'.",
                        "Normal component parameter must be of the form 'BnN', where 'N' is an integer.",
                    ]
                )
                cls._validate_order(key_num, msg)
            # validate skew component parameters 'BsN'
            elif key.startswith("Bs"):
                key_num = key[2:]
                msg = " ".join(
                    [
                        f"Invalid skew component parameter: '{key}'.",
                        "Skew component parameter must be of the form 'BsN', where 'N' is an integer.",
                    ]
                )
                cls._validate_order(key_num, msg)
            else:
                msg = " ".join(
                    [
                        f"Invalid magnetic multipole parameter: '{key}'.",
                        "Magnetic multipole parameters must be of the form 'tiltN', 'BnN', or 'BsN', where 'N' is an integer.",
                    ]
                )
                raise ValueError(msg)
        return values
