from clients.courses.CoursesClient import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CourseSchema

from clients.files.FilesClient import get_files_client
from clients.files.files_schema import CreateFileRequestSchema

from clients.users.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema

from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema()
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
create_file_request = CreateFileRequestSchema(upload_file="/Users/maksimkamenskii/Desktop/sova.png")
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,      
    created_by_user_id=create_user_response.user.id    
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema()
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)