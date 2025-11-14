from pydantic import BaseModel, HttpUrl, ConfigDict, Field
from tools.fakers import fake

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str = Field(alias="uploadFile")


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema

class GetFileQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    fileId: str

class GetFileResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    file: FileSchema