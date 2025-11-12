from typing import TypedDict

import httpx

from ..api_client import APIClient
from ..public_http_builder import get_public_http_client

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class UserCreateData(TypedDict):
    """Тип данных для создания пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class PublicUsersClient(APIClient):
    def __init__(self, client: httpx.Client):
        super().__init__(client)

    def create_user_api(self, data: UserCreateData) -> httpx.Response:
        """
        Создает пользователя в API.
        """
        return self.post("/api/v1/users", json=data)

  # Добавили новый метод
    def create_user(self, request: UserCreateData) -> User:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())