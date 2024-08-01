from sqlalchemy.orm import sessionmaker
from src.infraestructure.datasources import engine
from src.infraestructure.schemas.sql_alchemy_user_schema import SqlAlchemyUserSchema
from src.application.interfaces.repositories.user_repository_interface import UserRepositoryInterface
from src.application.dtos.user_dto import UserDto
import uuid

class SqlAlchemyUserRepository(UserRepositoryInterface):
  def __init__(self):
    Session = sessionmaker(bind=engine)
    self.session = Session()

  def index() -> list[UserDto]:
    return

  def index_by_id(self, user_id: str) -> UserDto | None:
    user_entity = self.session.query(SqlAlchemyUserSchema).filter_by(id=uuid.UUID(user_id)).first()

    if user_entity:
      return UserDto(id=user_entity.id, name=user_entity.name, email=user_entity.email)

  def index_by_email(self, user_email: str) -> UserDto | None:
    return

  def store(self, user: UserDto) -> None:
    return

  def update(self, user: UserDto) -> None:
    return

  def delete(self, user_id: str) -> None:
    return
