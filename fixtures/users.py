import pytest  # Импортируем pytest

# Импортируем API клиенты
from clients.auth.AuthenticationClient import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from pydantic import BaseModel, EmailStr
from clients.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.private_http_builder import AuthenticationUserSchema
from tools.assertions.users import assert_create_user_response

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password
    
    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)

# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response) 

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)