import httpx

data = {
  "email": "bruce@wayne.corp",
  "password": "123456"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью

access_token = response.json()["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)



print(response.status_code)  # 200
print(response.json())       # Ответ с информацией о пользователе