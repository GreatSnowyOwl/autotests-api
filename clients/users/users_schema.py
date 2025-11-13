from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры запроса получения пользователя.
    """
    user: UserSchema

class GetUserQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    userId: str