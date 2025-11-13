from pydantic import BaseModel, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class ExerciseInfoRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение информации о задании по exercise_id.
    """
    exerciseId: str

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str





class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение информации о заданиях.
    """
    exercises: list[ExerciseSchema]

class GetExerciseInfoResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    exercise: ExerciseSchema

class DeleteExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на удаление упражнения.
    """
    exercise: ExerciseSchema