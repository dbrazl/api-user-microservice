from pydantic import BaseModel, Field

class PydanticNameDto(BaseModel):
  name: str = Field(min_length=3)
