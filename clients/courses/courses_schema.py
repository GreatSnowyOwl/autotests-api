from pydantic import BaseModel, Field, constr, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake

class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: constr(min_length=1, max_length=100)
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: constr(min_length=1, max_length=1000)
    estimated_time: constr(min_length=1, max_length=100) = Field(alias="estimatedTime")
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: constr(min_length=1, max_length=100) = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: constr(min_length=1, max_length=1000,) = Field(default_factory=fake.text)
    estimated_time: constr(min_length=1, max_length=100) = Field(default_factory=fake.estimated_time, alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса получения списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    courses: list[CourseSchema]

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса обновления курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: constr(min_length=1, max_length=100) = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: constr(min_length=1, max_length=1000) = Field(default_factory=fake.text)
    estimated_time: constr(min_length=1, max_length=100) = Field(default_factory=fake.estimated_time, alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    course: CourseSchema

