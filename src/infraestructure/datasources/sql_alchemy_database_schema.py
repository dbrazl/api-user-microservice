from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.infraestructure.interfaces.datasources.database_schema_interface import DatabaseSchemaInterface

class SqlAlchemyDatabaseSchema(DatabaseSchemaInterface):
  def create_base_schema(self):
    metadata = MetaData()
    Base = declarative_base(metadata=metadata)
    return Base
