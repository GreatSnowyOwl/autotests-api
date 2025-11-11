from httpx import Client
from clients.users.public_users_client import PublicUsersClient, UserCreateData

client = Client()
users_api = PublicUsersClient(client)

user_data: UserCreateData = {
    "email": "test@example.com",
    "password": "string",
    "lastName": "Doe",
    "firstName": "John",
    "middleName": "Smith"
}

response = users_api.create_user_api(user_data)
print(response.status_code)
print(response.json())