from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str = Field(alias="description")
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias="courseId")

class ExerciseInfoRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение информации о задании по exercise_id.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercise_id: str = Field(alias="exerciseId")

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str | None = None
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int | None = Field(default_factory=lambda: fake.integer(1, 10), alias="orderIndex")
    description: str | None = None
    estimated_time: str | None = Field(default_factory=fake.estimated_time, alias="estimatedTime")

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