from flask import Blueprint, make_response, jsonify, request, Response
from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from src.infraestructure.dtos.user_response_dto import UserResponseDto
from src.infraestructure.dtos.validation_error_dto import ValidationErrorDto
from src.infraestructure.validators.flask_query_param_unexpected_filters_validator import flask_query_param_unexpected_filters_validator
from src.infraestructure.validators.flask_query_param_request_filters_together_validator import flask_query_param_request_filters_together_validator
from src.infraestructure.validators.flask_query_param_email_validator import flask_query_param_email_validator
from src.infraestructure.validators.flask_query_param_id_validator import flask_query_param_id_validator
from src.infraestructure.validators.flask_query_param_name_validator import flask_query_param_name_validator
from src.infraestructure.validators.flask_body_request_user_validator import flask_body_request_user_validator
from src.infraestructure.validators.flask_param_id_validator import flask_param_id_validator
from src.adapters.controllers.user_controller import UserController
from src.application.interfaces.network.http_status_interface import HttpStatusInterface
from src.application.interfaces.exceptions.exception_messages_interface import ExceptionMessagesInterface
from src.application.dtos.user_dto import UserDto
from src.application.exceptions.api_exception import ApiException

class FlaskUserRoutes:
  user_bp = Blueprint('user_bp', __name__)

  @staticmethod
  @user_bp.route('/health', methods=['GET'])
  def health(http_status: HttpStatusInterface) -> tuple[Response, int]:
    return make_response('', http_status.OK)

  @staticmethod
  @user_bp.route('/', methods=['GET'])
  @jwt_required()
  @flask_query_param_unexpected_filters_validator
  @flask_query_param_request_filters_together_validator
  @flask_query_param_email_validator
  @flask_query_param_id_validator
  @flask_query_param_name_validator
  def index(http_status: HttpStatusInterface, user_controller: UserController) -> tuple[Response, int]:
    filter = next(iter(request.args.keys()), None)
    filter_value = next(iter(request.args.values()), None)
    user_dto_or_list = user_controller.index(filter, filter_value)

    if isinstance(user_dto_or_list, list):
      dto_list = list(map(lambda user_dto: UserResponseDto(id=user_dto.id, name=user_dto.name, email=user_dto.email).to_dict(), user_dto_or_list))
      return dto_list

    dto = UserResponseDto(id=user_dto_or_list.id, name=user_dto_or_list.name, email=user_dto_or_list.email).to_dict()
    return jsonify(dto), http_status.OK

  @staticmethod
  @user_bp.route('/', methods=['POST'])
  @jwt_required()
  @flask_body_request_user_validator
  def store(http_status: HttpStatusInterface, user_controller: UserController) -> tuple[Response, int]:
    body = request.get_json()
    user = UserDto(id=None, name=body['name'], email=body['email'])
    user_controller.store(user)
    return make_response('', http_status.CREATED)

  @staticmethod
  @user_bp.route('/<string:id>', methods=['PUT'])
  @jwt_required()
  @flask_param_id_validator
  @flask_body_request_user_validator
  def update(id: str, http_status: HttpStatusInterface, user_controller: UserController) -> tuple[Response, int]:
    body = request.get_json()
    user = UserDto(id=id, name=body['name'], email=body['email'])
    user_controller.update(user)
    return make_response('', http_status.NO_CONTENT)

  @staticmethod
  @user_bp.route('/<string:id>', methods = ['DELETE'])
  @jwt_required()
  @flask_param_id_validator
  def delete(id: str, http_status: HttpStatusInterface, user_controller: UserController) -> tuple[Response, int]:
    user_controller.delete(id)
    return make_response('', http_status.OK)

  @staticmethod
  @user_bp.app_errorhandler(ValidationError)
  def handle_validation_error(
    error: ValidationError,
    exception_messages: ExceptionMessagesInterface,
    http_status: HttpStatusInterface
  ) -> tuple[Response, int]:
    dto = ValidationErrorDto(message=exception_messages.VALIDATION_ERROR, errors=error.errors()).to_dict()
    return dto, http_status.BAD_REQUEST


  @staticmethod
  @user_bp.app_errorhandler(ApiException)
  def handle_api_exception(error: ApiException) -> tuple[Response, int]:
    return jsonify({ "error": error.message }), error.status_code

  @staticmethod
  @user_bp.app_errorhandler(404)
  def handle_not_found_resource(
    error: Exception,
    exception_messages: ExceptionMessagesInterface,
    http_status: HttpStatusInterface
  ) -> tuple[Response, int]:
    return jsonify({ "error": exception_messages.RESOURCE_NOT_FOUNDED }), http_status.NOT_FOUND

  @staticmethod
  @user_bp.app_errorhandler(405)
  def handle_method_not_allowed(
    error: Exception,
    exception_messages: ExceptionMessagesInterface,
    http_status: HttpStatusInterface
  ) -> tuple[Response, int]:
    return jsonify({ "error": exception_messages.METHOD_NOT_ALLOWED }), http_status.METHOD_NOT_ALLOWED

  @staticmethod
  @user_bp.app_errorhandler(Exception)
  def handle_unexpected_exception(
    error: Exception,
    exception_messages: ExceptionMessagesInterface,
    http_status: HttpStatusInterface
  ) -> tuple[Response, int]:
    return jsonify({ "error": exception_messages.INTERNAL_SERVER_ERROR }), http_status.INTERNAL_SERVER_ERROR
