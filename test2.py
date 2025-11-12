import httpx
from httpx import Client
from clients.exercises.exercises_client import ExercisesClient, CreateExerciseRequestDict

client = Client()
exercises_api = ExercisesClient(client)

data = {
  "email": "bruce@wayne.corp",
  "password": "123456"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью

access_token = response.json()["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}

exercise_data: CreateExerciseRequestDict = {
    
  "title": "Introduction to Python Automation",
  "courseId": "QA-AUTO-101",
  "maxScore": 100,
  "minScore": 50,
  "orderIndex": 1,
  "description": "Learn the fundamentals of Python for automation testing, including HTTP requests, data handling, and test case design.",
  "estimatedTime": "2 hours"

}

response = exercises_api.create_exercise_api(exercise_data, headers=headers)
print(response.status_code)
print(response.json())