from sqlalchemy.orm import sessionmaker
from src.infraestructure.datasources import engine
from src.infraestructure.schemas.sql_alchemy_user_schema import SqlAlchemyUserSchema
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
import uuid

class SqlAlchemyUserRepository(UserRepositoryInterface):
  def __init__(self):
    Session = sessionmaker(bind=engine)
    self.session = Session()

  def index():
    return

  def index_one(self, user_id):
    return self.session.query(SqlAlchemyUserSchema).filter_by(id=uuid.UUID(user_id)).first()

  def index_by_email(self, user_email):
    return

  def store(self, user):
    return

  def update(self, user):
    return

  def delete(self, user_id):
    return
