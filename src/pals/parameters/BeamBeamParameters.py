from pydantic import BaseModel, ConfigDict


class BeamBeamParameters(BaseModel):
    """Beam-beam parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    # Parameters will be added when construction is complete
