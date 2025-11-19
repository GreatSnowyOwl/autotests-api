from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.users.private_http_builder import AuthenticationUserSchema
from tests.conftest import UserFixture
import pytest
from pydantic import BaseModel
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)