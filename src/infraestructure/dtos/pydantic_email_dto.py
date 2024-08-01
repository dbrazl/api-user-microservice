from pydantic import BaseModel, EmailStr

class PydanticEmailDto(BaseModel):
  email: EmailStr
