import asyncio
import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        # Отправляем 5 ответов с задержкой
        for i in range(1, 6):
            response = f"{i} Cообщение пользователя — {message}"
            await websocket.send(response)
            await asyncio.sleep(1)  # необязательная задержка между ответами


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())