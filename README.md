# Каталог рецептов

Проект доступен по адресу: http://127.0.0.1:8000

Панель управления: http://127.0.0.1:8000/admin/

## Настройка проекта
Для управления проектом используйте команды, описанные ниже.

Создайте `.env` файл в корне репозитория:

```bash
$ cp .env.dist .env
```

Внесите необходимые изменения в переменные окружения `SECRET_KEY`, `DB_USER`, `DB_PASSWORD`.

Для сборки и запуска контейнеров в фоновом режиме используйте следующую команду:
```bash
$  docker-compose up --build -d
```
После сборки и запуска контейнеров команды выполняются внутри контейнера приложения следующим образом:
```bash
$ docker-compose exec web <command>
```
Для заполнения БД тестовыми данными используйте следующую команду:
```bash
$ docker-compose exec web python manage.py loaddata product recipe ingredient
```
Для добавления рецептов через панель управления нужно создать суперпользователя с помощью команды:
```bash
$ docker-compose exec web python manage.py createsuperuser
```

## Работа с Docker
### Просмотр логов:
```bash
$ docker-compose logs <container>
```

### Остановка контейнеров:

```bash
$ docker-compose stop
```

### Остановка и удаление контейнеров вместе с томами:

```bash
$ docker-compose down --volumes
```
