from pydantic import BaseModel, ConfigDict


class TrackingParameters(BaseModel):
    """Tracking parameters"""

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    # Parameters will be added when construction is complete
