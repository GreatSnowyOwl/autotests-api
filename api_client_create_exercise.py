from clients.courses.CoursesClient import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CourseSchema

from clients.files.FilesClient import get_files_client
from clients.files.files_schema import CreateFileRequestSchema

from clients.users.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema

from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema

from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)
# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_response.user.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)
# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="/Users/maksimkamenskii/Desktop/sova.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema(
    title="Introduction to Python",
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=1,
    description="Learn the fundamentals of Python for automation testing, including HTTP requests, data handling, and test case design.",
    estimated_time="4 hours"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)