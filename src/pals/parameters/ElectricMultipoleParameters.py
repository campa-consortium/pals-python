from pydantic import BaseModel, ConfigDict


class ElectricMultipoleParameters(BaseModel):
    """Electric multipole parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    # Parameters will be added when construction is complete
