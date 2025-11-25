from http import HTTPStatus

import pytest

from clients.files.FilesClient import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response
from tools.assertions.schema import validate_json_schema
from clients.files.files_schema import GetFileQuerySchema
from clients.files.files_schema import GetFileResponseSchema
from tools.assertions.files import assert_get_file_with_incorrect_file_id_response
from clients.errors_schema import ValidationErrorResponseSchema
from tools.tags import AllureTag
from tools.epics import AllureEpic
from tools.features import AllureFeature
from allure_commons.types import Severity
import allure
from tools.stories import AllureStory




@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.FILES)  # Добавили feature
@allure.severity(Severity.CRITICAL)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.FILES)
class TestFiles:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.title("Create file")
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="/Users/maksimkamenskii/Desktop/sova.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)  # Добавили story
    @allure.title("Get file with incorrect file id")
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        """
    Негативный тест: проверяет получение файла с некорректным file_id.
    
    Ожидается ошибка валидации 422 (UNPROCESSABLE_ENTITY) при передаче 
    некорректного UUID в качестве file_id.
        """
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
