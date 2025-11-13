from pydantic import BaseModel, HttpUrl, ConfigDict


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
    filename: str
    directory: str
    upload_file: str


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