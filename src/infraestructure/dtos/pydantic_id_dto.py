from pydantic import BaseModel, UUID4

class PydanticIdDto(BaseModel):
  id: UUID4
