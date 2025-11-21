from tools.assertions.base import assert_equal
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema

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