from src.infraestructure.config.config import Config

class SqlAlchemyEnvironmentManager:
  def __init__(self, base, engine):
    self.Base = base
    self.engine = engine

  def listen_changes(self):
    if Config.ENVIRONMENT == 'DEVELOPER':
      from src.infrastructure.schemas.sql_alchemy_user_schema import SqlAlchemyUserSchema
      self.Base.metadata.create_all(self.engine)
