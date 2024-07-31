from sqlalchemy import create_engine
from src.infraestructure.config.config import Config
from src.core.interfaces.datasources.database_connector_interface import DatabaseConnectorInterface

class SqlAlchemyDatabaseConnector(DatabaseConnectorInterface):
  def connect(self):
    engine = create_engine(Config.DATABASE_URL)
    return engine
