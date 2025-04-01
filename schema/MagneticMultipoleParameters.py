from pydantic import BaseModel, ConfigDict, model_validator
from typing import Any, Dict


class MagneticMultipoleParameters(BaseModel):
    """Magnetic multipole parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    # Custom validation to be applied before standard validation
    @model_validator(mode="before")
    def validate(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        # loop over all attributes
        for key in values:
            # validate tilt parameters 'tiltN'
            if key.startswith("tilt"):
                key_num = key[4:]
                if key_num.isdigit():
                    if key_num.startswith("0") and key_num != "0":
                        raise ValueError(
                            " ".join(
                                [
                                    f"Invalid tilt parameter: '{key}'.",
                                    "Leading zeros are not allowed.",
                                ]
                            )
                        )
                else:
                    raise ValueError(
                        " ".join(
                            [
                                f"Invalid tilt parameter: '{key}'.",
                                "Tilt parameter must be of the form 'tiltN', where 'N' is an integer.",
                            ]
                        )
                    )
            else:
                raise ValueError(
                    " ".join(
                        [
                            f"Invalid tilt parameter: '{key}'.",
                            "Tilt parameter must be of the form 'tiltN', where 'N' is an integer.",
                        ]
                    )
                )
        return values
