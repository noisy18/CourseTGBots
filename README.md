# Запуск проекта:
- Открываем терминал (в директории, где находиться docker-compose.yml, то есть корневой)
- Далее открываем Docker Desktop

- Вводим команду в терминал: __docker-compose up --build__

*Если возникают ошибки, проверьте, чтобы все requirements были соблюдены.*

- После чего перезапускаем проект командами:
__docker-compose down -v__
__docker-compose up --build__ или __docker-compose up -d --build__ (для запуска в фоновом режиме)


# Просмотр документации (Swagger):
Переходим по адресу:

`http:/localhost:8000/docs`

# API Documentation

## ENDPOINT - Tokens
`POST /tokens`  
Получение JWT токена

**Request:**
```json
{
  "email": "user@example.com"
}
```

**Response (Success):**
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

**Response (Error):**
```json
{
  "detail": "Incorrect email"
}
```

`GET /tokens`

**Request:**

Headers:
| Key  | Value     |
|-----------|---------|
| Authorization     | Bearer `JWT`  |

**Response (Success):**
```json
{
    "access": true,
    "email": "user@example.com"
}