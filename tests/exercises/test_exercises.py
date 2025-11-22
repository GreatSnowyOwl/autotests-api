from httpx import RequestNotRead
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
import pytest
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_update_exercise_response
from tools.assertions.schema import validate_json_schema
from fixtures.exercises import ExerciseFixture
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.exercises import assert_get_exercises_response

@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        """Проверяет успешное создание упражнения через POST /api/v1/exercises."""
        request = CreateExerciseRequestSchema()
        request.course_id = function_course.response.course.id
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_get_exercises(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное получение списка упражнений через GET /api/v1/exercises."""
        request = GetExercisesQuerySchema(exercise_id=function_exercise.response.exercise.id, course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
    
    def test_update_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное обновление упражнения через PATCH /api/v1/exercises/{exercise_id}."""
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.response.exercise.id, request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())