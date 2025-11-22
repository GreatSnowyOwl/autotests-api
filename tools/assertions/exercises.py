from tools.assertions.base import assert_equal
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base import assert_length
from clients.exercises.exercises_schema import GetExercisesResponseSchema , ExerciseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.errors import assert_internal_error_response
from clients.errors_schema import InternalErrorResponseSchema

def assert_create_exercise_response(
    create_exercise_request: CreateExerciseRequestSchema,
    create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу.

    :param create_exercise_request: Исходный запрос на создание упражнения.
    :param create_exercise_response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(create_exercise_response.exercise.title, create_exercise_request.title, "title")
    assert_equal(create_exercise_response.exercise.course_id, create_exercise_request.course_id, "course_id")
    assert_equal(create_exercise_response.exercise.max_score, create_exercise_request.max_score, "max_score")
    assert_equal(create_exercise_response.exercise.min_score, create_exercise_request.min_score, "min_score")
    assert_equal(create_exercise_response.exercise.order_index, create_exercise_request.order_index, "order_index")
    assert_equal(create_exercise_response.exercise.description, create_exercise_request.description, "description")
    assert_equal(create_exercise_response.exercise.estimated_time, create_exercise_request.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")

def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseSchema,
    create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка упражнений соответствует ответам на их создание.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")
    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)

def assert_update_exercise_response(
    update_exercise_request: UpdateExerciseRequestSchema,
    update_exercise_response: UpdateExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление упражнения соответствует запросу.
    """
    assert_equal(update_exercise_response.exercise.title, update_exercise_request.title, "title")
    assert_equal(update_exercise_response.exercise.max_score, update_exercise_request.max_score, "max_score")
    assert_equal(update_exercise_response.exercise.min_score, update_exercise_request.min_score, "min_score")
    assert_equal(update_exercise_response.exercise.description, update_exercise_request.description, "description")
    assert_equal(update_exercise_response.exercise.estimated_time, update_exercise_request.estimated_time, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ на получение информации о упражнении не найден.
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)