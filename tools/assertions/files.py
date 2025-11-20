from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base import assert_equal
from clients.errors_schema import ValidationErrorResponseSchema
from clients.errors_schema import ValidationErrorSchema
from tools.assertions.errors import assert_validation_error_response

def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Формируем ожидаемую ссылку на загруженный файл
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    '''
    Проверяет, что ответ на запрос получения файла с некорректным идентификатором файла соответствует ожидаемому значению.
    '''
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",  # Тип ошибки, связанной с слишком короткой строкой.
                input="incorrect-file-id",  # Некорректный идентификатор файла.
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},  # Контекст ошибки.
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",  # Сообщение об ошибке.
                location=["path", "file_id"]  # Поле, в котором возникла ошибка.
            )
        ]
    )
    assert_validation_error_response(actual, expected)