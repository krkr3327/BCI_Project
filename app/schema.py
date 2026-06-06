from pydantic import BaseModel, Field

class CommandRequest(BaseModel):
    command: str
    confidence: float = Field(
        ge=0.0,
        le=1.0
    )