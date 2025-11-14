import jsonschema
from pydantic import BaseModel
from clients.users.public_users_client import get_public_users_client
from clients.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from clients.users.private_http_builder import AuthenticationUserSchema
# Добавили импорт функции validate_json_schema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()


create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
# Получаем JSON схему из модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=create_user_response.model_dump(by_alias=True), schema=create_user_response_schema)

# Создаем объект AuthenticationUserSchema для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_response.user.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

print("✅ Все проверки пройдены!")
print(f"User data: {get_user_response.json()}")

