from pydantic import BaseModel, EmailStr, Field

class PydanticUserDto(BaseModel):
  name: str = Field(min_length=3)
  email: EmailStr
