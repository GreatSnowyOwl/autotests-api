import httpx

from tools.fakers import get_random_email

email = get_random_email()
password = "string"

payload = {
    "email": email,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

user_id = response.json()["user"]["id"]

data= {
  "email": email,
  "password": password,
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)

access_token = response.json()["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}

patch_data =  {
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=patch_data, headers=headers)

print(response.status_code)
print(response.json())