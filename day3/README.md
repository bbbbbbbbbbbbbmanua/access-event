# Day 3 — Backend AccessEvent
# AccessEvent — День 3: Backend на Python/Flask

Инклюзивная платформа мероприятий. Backend-часть: REST API, модели БД, JWT-аутентификация.

## Что реализовано

### Модели базы данных (`models.py`)
- **User** — пользователи (роли: `user`, `organizer`, `admin`), поля инклюзивности (`is_deaf`, `accessibility_needs`)
- **Event** — мероприятия с полями доступности (`is_inclusive`, `sign_language`, `visual_alerts`)
- **Registration** — регистрация на мероприятия со статусами `pending` / `confirmed` / `cancelled`

Ограничения на уровне БД:
- `UNIQUE(email)` у пользователя
- `UNIQUE(user_id, event_id)` у регистрации — один пользователь не может записаться дважды
- `CHECK(status IN ('pending', 'confirmed', 'cancelled'))`

### API-эндпоинты

| Метод | URL | Доступ | Описание |
|---|---|---|---|
| POST | `/api/register` | все | Регистрация пользователя |
| POST | `/api/login` | все | Вход, получение JWT-токена |
| GET | `/api/events` | все | Список мероприятий (фильтр `?inclusive=1`) |
| GET | `/api/events/<id>` | все | Одно мероприятие |
| POST | `/api/events` | organizer | Создание мероприятия |
| PUT | `/api/events/<id>` | organizer | Редактирование (только свои) |
| DELETE | `/api/events/<id>` | organizer | Удаление (только свои) |
| POST | `/api/registrations` | user | Запись на мероприятие |
| GET | `/api/registrations` | user | Свои регистрации |
| PUT | `/api/registrations/<id>` | organizer | Изменение статуса регистрации |

### Аутентификация
- **JWT-токены** (HS256), срок жизни — 24 часа
- Заголовок `Authorization: Bearer <token>`
- Пароли хранятся **хешированными** (PBKDF2 через `werkzeug.security`)

### Инклюзивность (по ТЗ)
- Поля `is_inclusive`, `sign_language`, `visual_alerts` у мероприятий
- Флаг `is_deaf` и `accessibility_needs` у пользователей
- Фильтр инклюзивных мероприятий через `?inclusive=1`
- Валидация потребностей доступности при регистрации

## Структура проект
