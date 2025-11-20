from typing import TypedDict

from httpx import Response, Headers

from clients.api_client import APIClient

from clients.users.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, ExerciseInfoRequestSchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseInfoResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema, DeleteExerciseResponseSchema


# Клиент для работы с /api/v1/exercises - упражнения
class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises_info_api(self, request: ExerciseInfoRequestSchema, headers: Headers | dict | None = None) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param query: Словарь с exerciseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{request.exerciseId}",json=request.model_dump(by_alias=True),headers=headers)


    def create_exercise_api(self, request: CreateExerciseRequestSchema, headers: Headers | dict | None = None) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True), headers=headers)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema, headers: Headers | dict | None = None) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True), headers=headers)

    def delete_exercise_api(self, exercise_id: str, headers: Headers | dict | None = None) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}", headers=headers)
       # Добавили новый метод создания упражнения
    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)
    
    # Добавили новый метод получения списка упражнений
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)
    
    # Добавили новый метод получения информации о задании по exercise_id
    def get_exercise_info(self, request: ExerciseInfoRequestSchema) -> GetExerciseInfoResponseSchema:
        response = self.get_exercise_info_api(request)
        return GetExerciseInfoResponseSchema.model_validate_json(response.text)
    
    # Добавили новый метод обновления упражнения
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)
    
    # Добавили новый метод удаления упражнения
    def delete_exercise(self, exercise_id: str) -> DeleteExerciseResponseSchema:
        response = self.delete_exercise_api(exercise_id)
        return DeleteExerciseResponseSchema.model_validate_json(response.text)    
    
# Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))