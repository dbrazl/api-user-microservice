from pydantic import BaseModel, EmailStr, Field

class PydanticUserRequestDto(BaseModel):
  name: str = Field(min_length=3)
  email: EmailStr
