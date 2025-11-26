from typing import Any
import allure
from httpx import Client, URL, Response, QueryParams, Headers
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client, base_url: str = "http://localhost:8000"):
        self.client = client
        self.base_url = base_url

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None, headers: Headers | dict | None = None) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :param headers: HTTP заголовки запроса.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(f"{self.base_url}{url}", params=params, headers=headers)

    @allure.step("Make POST request to {url}")
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
            headers: Headers | dict | None = None
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :param headers: HTTP заголовки запроса.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(f"{self.base_url}{url}", json=json, data=data, files=files, headers=headers)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None, headers: Headers | dict | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :param headers: HTTP заголовки запроса.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(f"{self.base_url}{url}", json=json, headers=headers)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str, headers: Headers | dict | None = None) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :param headers: HTTP заголовки запроса.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(f"{self.base_url}{url}", headers=headers)

                  
