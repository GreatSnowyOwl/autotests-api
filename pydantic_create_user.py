from pydantic import BaseModel, EmailStr, constr, alias

# Модель пользователя
class UserSchema(BaseModel):
    id: str 
    email: EmailStr
    last_name: constr(min_length=1, max_length=15, alias= "lastName")
    first_name: constr(min_length=1, max_length=15, alias= "firstName")
    middle_name: str(alias= "middleName")

# Модель запроса на создание пользователя
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    last_name: constr(min_length=1, max_length=15, alias= "lastName")
    first_name: constr(min_length=1, max_length=15, alias= "firstName")
    middle_name: str

# Модель ответа на создание пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema
