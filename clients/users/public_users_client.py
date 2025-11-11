from typing import TypedDict

import httpx

from ..api_client import APIClient


class UserCreateData(TypedDict):
    """Тип данных для создания пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def __init__(self, client: httpx.Client):
        super().__init__(client)

    def create_user_api(self, data: UserCreateData) -> httpx.Response:
        """
        Создает пользователя в API.
        """
        return self.post("/api/v1/users", json=data)

