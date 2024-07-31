from src.infraestructure.config.config import Config
from src.infraestructure.interfaces.datasources.environment_manager_interface import EnvironmentManagerInterface

class SqlAlchemyEnvironmentManager(EnvironmentManagerInterface):
  def __init__(self, base, engine):
    self.Base = base
    self.engine = engine

  def listen_dev_db_changes(self):
    if Config.ENVIRONMENT == 'DEVELOPER':
      from src.infraestructure.schemas.sql_alchemy_user_schema import SqlAlchemyUserSchema
      self.Base.metadata.create_all(self.engine)
