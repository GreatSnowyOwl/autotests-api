from pydantic import BaseModel, constr, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema



class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: constr(min_length=1, max_length=100)
    maxScore: int
    minScore: int
    description: constr(min_length=1, max_length=1000)
    estimatedTime: constr(min_length=1, max_length=100)
    previewFile: FileSchema
    createdByUser: UserSchema


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: constr(min_length=1, max_length=100)
    maxScore: int
    minScore: int
    description: constr(min_length=1, max_length=1000)
    estimatedTime: constr(min_length=1, max_length=100)
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    userId: str

class GetCoursesResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    courses: list[CourseSchema]

class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: constr(min_length=1, max_length=100) | None
    maxScore: int | None
    minScore: int | None
    description: constr(min_length=1, max_length=1000) | None
    estimatedTime: constr(min_length=1, max_length=100) | None
