FastAPI Blog API

📌 Описание

Этот проект создан для изучения FastAPI и представляет собой API для управления блогами и пользователями.
Реализованы CRUD-операции для блогов и пользователей, а также система аутентификации.
В качестве базы данных используется MySQL с SQLAlchemy.

🚀 Установка и запуск

1. Клонирование репозитория

>>git clone https://github.com/GlebSavenyuk/test_FastAPI.git
>>cd test_FastAPI

2. Создание виртуального окружения и установка зависимостей

>>python -m venv venv
>>source venv/bin/activate  # для macOS/Linux
>>venv\Scripts\activate  # для Windows
>>pip install -r requirements.txt

3. Настройка базы данных (MySQL)

1.Убедитесь, что MySQL запущен.

2.Создайте базу данных:

CREATE DATABASE fastapi_blog;

4. Запуск сервера

>>uvicorn blog.main:app --reload

После запуска сервер будет доступен по адресу: http://127.0.0.1:8000

📜 API Эндпоинты

🔹 Блоги

Метод   Эндпоинт     Описание

GET     /blog/       Получить все блоги

POST    /blog/       Создать блог

GET     /blog/{id}   Получить блог по ID

PUT     /blog/{id}   Обновить блог

DELETE  /blog/{id}   Удалить блог

🔹 Пользователи

Метод   Эндпоинт   Описание

POST    /user/     Создать пользователя

GET     /user/{id} Получить пользователя

🔹 Аутентификация

Метод   Эндпоинт   Описание

POST    /login    Вход в систему

📌 Схемы

Blog

User

ShowBlog

ShowUser

Body_login_login_post

HTTPValidationError

ValidationError

🛠 Технологии

FastAPI — фреймворк для API

SQLAlchemy — ORM для работы с MySQL

Pydantic — валидация данных

Uvicorn — ASGI-сервер для FastAPI


