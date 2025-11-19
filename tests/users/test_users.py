import pytest
from clients.private_users_client import PrivateUsersClient
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.users import assert_get_user_response
from clients.users.public_users_client import PublicUsersClient, CreateUserRequestSchema
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake

@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client: PrivateUsersClient, function_user):
    get_user_response_raw= private_users_client.get_user_me_api()
    get_user_response = GetUserResponseSchema.model_validate(get_user_response_raw.json())
    assert_status_code(get_user_response_raw.status_code, HTTPStatus.OK)
    assert_get_user_response(
        get_user_response=get_user_response,        # Данные из GET /users/me
        create_user_response=function_user.response  # Данные из POST /users (фикстура)
           )
    validate_json_schema(get_user_response_raw.json(), GetUserResponseSchema.model_json_schema())

@pytest.mark.regression
@pytest.mark.users
@pytest.mark.parametrize("domain", ["mail.ru","gmail.com", "example.com"])
def test_create_user(public_users_client: PublicUsersClient, domain: str):
    create_user_request = CreateUserRequestSchema(email=fake.email(domain=domain))
    create_user_response_raw = public_users_client.create_user_api(create_user_request)
    create_user_response = CreateUserResponseSchema.model_validate(create_user_response_raw.json())
    assert_status_code(create_user_response_raw.status_code, HTTPStatus.OK)
    assert_create_user_response(request=create_user_request, response=create_user_response)
    validate_json_schema(instance=create_user_response.model_dump(by_alias=True), schema=CreateUserResponseSchema.model_json_schema())