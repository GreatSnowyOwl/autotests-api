from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal
from clients.users.users_schema import GetUserResponseSchema, UserSchema


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual_user: UserSchema, expected_user: UserSchema):
   
    """
    Сравнивает два объекта UserSchema.
    
    :param actual_user: Фактические данные пользователя.
    :param expected_user: Ожидаемые данные пользователя.
    :raises AssertionError: Если данные не совпадают.
    """
    assert_equal(actual_user.id, expected_user.id, "id")
    assert_equal(actual_user.email, expected_user.email, "email")
    assert_equal(actual_user.last_name, expected_user.last_name, "last_name")
    assert_equal(actual_user.first_name, expected_user.first_name, "first_name")
    assert_equal(actual_user.middle_name, expected_user.middle_name, "middle_name")

def assert_get_user_response(create_user_response: CreateUserResponseSchema, get_user_response: GetUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя соответствует запросу.

    :param create_user_response: Ответ на создание пользователя.
    :param get_user_response: Ответ на получение пользователя.
    :raises AssertionError: Если данные не совпадают.
    """
    assert_user(get_user_response.user, create_user_response.user)

