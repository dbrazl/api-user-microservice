from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.core.interfaces.datasources.database_schema_interface import DatabaseSchemaInterface

class SqlAlchemyDatabaseSchema(DatabaseSchemaInterface):
  def create_base(self):
    metadata = MetaData()
    Base = declarative_base(metadata=metadata)
    return Base
