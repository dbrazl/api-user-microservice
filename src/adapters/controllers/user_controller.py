from flask import Blueprint, make_response, jsonify, request
from src.adapters.models.user_response_dto import UserResponseDto
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.factories.index_users_factory_interface import IndexUsersFactoryInterface
from src.application.exceptions.api_exception import ApiException
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface

class UserController:
  user_bp = Blueprint('user_bp', __name__)

  @staticmethod
  @user_bp.route('/health', methods=['GET'])
  def health(http_status: HttpStatusInterface):
    return make_response('', http_status.OK)

  @staticmethod
  @user_bp.route('/', methods=['GET'])
  def index(http_status: HttpStatusInterface, index_users_factory: IndexUsersFactoryInterface):
    filter = next(iter(request.args.keys()), None)
    filter_value = next(iter(request.args.values()), None)
    index_use_case = index_users_factory.make_index_use_case(filter)
    user_dto_or_list = index_use_case.execute(filter_value) if filter else index_use_case.execute()

    if isinstance(user_dto_or_list, list):
      dto_list = list(map(lambda user_dto: UserResponseDto(id=user_dto.id, name=user_dto.name, email=user_dto.email).to_dict(), user_dto_or_list))
      return dto_list

    dto = UserResponseDto(id=user_dto_or_list.id, name=user_dto_or_list.name, email=user_dto_or_list.email).to_dict()
    return jsonify(dto), http_status.OK

  @staticmethod
  @user_bp.app_errorhandler(ApiException)
  def handle_api_exception(error):
    return jsonify({ "error": error.message }), error.status_code

  @staticmethod
  @user_bp.app_errorhandler(404)
  def handle_not_found_resource(error, exception_messages: ExceptionMessagesInterface, http_status: HttpStatusInterface):
    return jsonify({ "error": exception_messages.RESOURCE_NOT_FOUNDED }), http_status.NOT_FOUND

  @staticmethod
  @user_bp.app_errorhandler(Exception)
  def handle_unexpected_exception(error, exception_messages: ExceptionMessagesInterface, http_status: HttpStatusInterface):
    print(error)
    return jsonify({ "error": exception_messages.INTERNAL_SERVER_ERROR }), http_status.INTERNAL_SERVER_ERROR
