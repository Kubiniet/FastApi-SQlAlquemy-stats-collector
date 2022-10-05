# stats_collector

Этот проект был создан с использованием fastapi_template.

## Docker

Вы можете запустить проект с докером, используя эту команду:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

Если вы хотите разрабатывать в докере с автоматической перезагрузкой, добавьте `-f deploy/docker-compose.dev.yml` в свою команду докера.
Как это:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up
```

## Структура проекта

```bash
$ tree "stats_collector"
stats_collector
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to inteact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Конфигурация

Это приложение можно настроить с помощью переменных среды.

Вы можете создать файл `.env` в корневом каталоге и поместить все
переменные окружения здесь.

Все переменные среды должны начинаться с префикса «STATS_COLLECTOR_».

Например, если вы видите в своем «stats_collector/settings.py» переменную с именем вроде
`random_parameter`, вы должны предоставить "STATS_COLLECTOR_RANDOM_PARAMETER"
переменная для настройки значения. Это поведение можно изменить, переопределив свойство env_prefix.
в `stats_collector.settings.Settings.Config`.

Пример файла .env:
```bash
STATS_COLLECTOR_RELOAD="True"
STATS_COLLECTOR_PORT="8000"
STATS_COLLECTOR_ENVIRONMENT="dev"
```

## Миграции

Если вы хотите перенести свою базу данных, вам следует выполнить следующие команды:
```bash
# To run all migrations untill the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Отмена миграции

Если вы хотите отменить миграцию,  вам следует выполнить следующие команды::
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Генерация миграции

Для создания миграции вы должны запустить:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Запуск тестов

Если вы хотите запустить его в докере, просто запустите:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . run --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml --project-directory . down
```

## Скриншоты

### 1. Документация

![image](https://user-images.githubusercontent.com/96630622/194137506-b06685bc-6e4e-4d2e-a050-4b40ab8bd72c.png)

### 2. Метод показа статистики get()

![image](https://user-images.githubusercontent.com/96630622/194137422-4e5dc1fc-9a8a-4d6c-80a7-dd8bb1a4da92.png)

### 3. Метод сохранения статистики put()

![image](https://user-images.githubusercontent.com/96630622/194137613-2b7f68af-c407-4d73-a774-407b375035b8.png)

### 4. Метод сброса статистики delete()

![image](https://user-images.githubusercontent.com/96630622/194137686-e98e3cba-5e43-49a3-a367-fcdf01c730b6.png)
