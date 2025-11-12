from clients.courses.CoursesClient import get_courses_client, CreateCourseRequestDict
from clients.FilesClient import get_files_client, CreateFileRequestDict
from clients.users.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, UserCreateData, CreateUserResponseDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = UserCreateData(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)
# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)
# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="/Users/maksimkamenskii/Desktop/sova.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем упражнение
create_exercise_request = CreateExerciseRequestDict(
    title="Introduction to Python",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description="Learn the fundamentals of Python for automation testing, including HTTP requests, data handling, and test case design.",
    estimatedTime="4 hours"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)