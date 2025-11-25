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
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, ExerciseInfoRequestSchema
from tools.assertions.exercises import assert_get_exercises_response
from tools.assertions.exercises import assert_exercise_not_found_response
from clients.errors_schema import InternalErrorResponseSchema
from tools.epics import AllureEpic
from tools.features import AllureFeature
from tools.stories import AllureStory
from allure_commons.types import Severity
import allure
from tools.tags import AllureTag

@pytest.mark.exercises
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.story(AllureStory.CREATE_ENTITY)
@allure.severity(Severity.CRITICAL)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        """Проверяет успешное создание упражнения через POST /api/v1/exercises."""
        request = CreateExerciseRequestSchema()
        request.course_id = function_course.response.course.id
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())




    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_exercises(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное получение списка упражнений через GET /api/v1/exercises."""
        request = GetExercisesQuerySchema(exercise_id=function_exercise.response.exercise.id, course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
    
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное обновление упражнения через PATCH /api/v1/exercises/{exercise_id}."""
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.response.exercise.id, request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное удаление упражнения через DELETE /api/v1/exercises/{exercise_id}."""
        response = exercises_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        request_info = ExerciseInfoRequestSchema(exercise_id=function_exercise.response.exercise.id)
        response2 = exercises_client.get_exercise_info_api(request_info)
        response_data2 = InternalErrorResponseSchema.model_validate_json(response2.text)
        assert_status_code(response2.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(response_data2)
        validate_json_schema(response2.json(), response_data2.model_json_schema())


    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercises(self, exercises_client: ExercisesClient, function_course: CourseFixture, function_exercise: ExerciseFixture):
        """Проверяет успешное получение информации о задании по exercise_id через GET /api/v1/exercises/{exercise_id}."""
        request = GetExercisesQuerySchema(course_id=function_course.response.course.id, exercise_id=function_exercise.response.exercise.id)
        response = exercises_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())