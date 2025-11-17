import pytest
from clients.private_users_client import PrivateUsersClient
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.users import assert_get_user_response
from tests.conftest import UserFixture


@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client: PrivateUsersClient, function_user: UserFixture):
    get_user_response_raw= private_users_client.get_user_me_api()
    get_user_response = GetUserResponseSchema.model_validate(get_user_response_raw.json())
    assert_status_code(get_user_response_raw.status_code, HTTPStatus.OK)
    assert_get_user_response(
        get_user_response=get_user_response,        # Данные из GET /users/me
        create_user_response=function_user.response  # Данные из POST /users (фикстура)
           )
    validate_json_schema(get_user_response_raw.json(), GetUserResponseSchema.model_json_schema())

