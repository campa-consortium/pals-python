from pydantic import BaseModel, ConfigDict


class ElectricMultipoleParameters(BaseModel):
    """Electric multipole parameters"""

    # Allow arbitrary fields (TODO: remove this)
    model_config = ConfigDict(extra="allow")

    # TODO: add ElectricMultipoleParameters in a follow-up RP
    # https://pals-project.readthedocs.io/en/latest/element-parameters.html#electricmultipolep-electric-multipole-parameters
