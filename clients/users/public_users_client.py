from typing import TypedDict

import httpx

from ..api_client import APIClient
from ..public_http_builder import get_public_http_client
from ..users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema , GetUserResponseSchema , GetUserQuerySchema

class PublicUsersClient(APIClient):
    def __init__(self, client: httpx.Client):
        super().__init__(client)

    def create_user_api(self, data: CreateUserRequestSchema) -> httpx.Response:
        """
        Создает пользователя в API.
        """
        return self.post("/api/v1/users", json=data.model_dump(by_alias=True))

  # Добавили новый метод
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())