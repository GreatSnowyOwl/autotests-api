from typing import TypedDict

from httpx import Response, Headers

from clients.api_client import APIClient

from clients.users.private_http_builder import AuthenticationUserDict, get_private_http_client

# Типы запросов и ответов

class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class ExerciseInfoRequestDict(TypedDict):
    """
    Описание структуры запроса на получение информации о задании по exercise_id.
    """
    exerciseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str



class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры запроса на получение информации о заданиях.
    """
    exercises: list[Exercise]

class GetExerciseInfoResponseDict(TypedDict):
    exercises: list[Exercise]

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    exercise: Exercise

class DeleteExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на удаление упражнения.
    """
    exercise: Exercise

# Клиент для работы с /api/v1/exercises - упражнения
class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises_info_api(self, request: ExerciseInfoRequestDict, headers: Headers | dict | None = None) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param query: Словарь с exerciseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{request['exerciseId']}",json=request,headers=headers)


    def create_exercise_api(self, request: CreateExerciseRequestDict, headers: Headers | dict | None = None) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request, headers=headers)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict, headers: Headers | dict | None = None) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request, headers=headers)

    def delete_exercise_api(self, exercise_id: str, headers: Headers | dict | None = None) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param headers: HTTP заголовки запроса (например, Authorization).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}", headers=headers)
       # Добавили новый метод создания упражнения
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()
    
    # Добавили новый метод получения списка упражнений
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()
    
    # Добавили новый метод получения информации о задании по exercise_id
    def get_exercise_info(self, request: ExerciseInfoRequestDict) -> GetExerciseInfoResponseDict:
        response = self.get_exercise_info_api(request)
        return response.json()
    
    # Добавили новый метод обновления упражнения
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()
    
    # Добавили новый метод удаления упражнения
    def delete_exercise(self, exercise_id: str) -> DeleteExerciseResponseDict:
        response = self.delete_exercise_api(exercise_id)
        return response.json()
    
# Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Объект AuthenticationUserDict с email и паролем пользователя.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))