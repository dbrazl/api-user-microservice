from src.infraestructure.datasources.sql_alchemy_database_connector import SqlAlchemyDatabaseConnector
from src.infraestructure.datasources.sql_alchemy_database_schema import SqlAlchemyDatabaseSchema
from src.infraestructure.datasources.sql_alchemy_environment_manager import SqlAlchemyEnvironmentManager

database_connector = SqlAlchemyDatabaseConnector()
engine = database_connector.connect()

database_schema = SqlAlchemyDatabaseSchema()
Base = database_schema.create_base_schema()

environment_manager = SqlAlchemyEnvironmentManager(Base, engine)
environment_manager.listen_dev_db_changes()

__all__ = ["engine", "Base"]
