from src.infraestructure.datasources import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

class SqlAlchemyUserSchema(Base):
  __tablename__ = 'users'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
  name = Column(String)
  email = Column(String, unique=True, nullable=False, index=True)
