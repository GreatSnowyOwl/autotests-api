import socket

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")


# Закрываем соединение
client_socket.close()

# Создаем новый сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаемся к серверу 2
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Отправляем сообщение серверу 2
message = "Как дела?"
client_socket.send(message.encode())

# Получаем ответ от сервера 2
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

# Закрываем соединение
client_socket.close()