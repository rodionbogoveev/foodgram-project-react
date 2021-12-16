[![Foodgram workflow](https://github.com/rodionbogoveev/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/rodionbogoveev/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

# Проект Foodgram
Проект Foodgram - это сайт «Продуктовый помощник». На этом сервисе пользователи могут регистрироваться, публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект запущен и доступен по адресу http://62.84.119.90/recipes
# Технологии
В проекте применяются:
- **Python 3.7.9**
- **Django REST Framework**
- **Djoser**
- **PostgreSQL**
- **Docker**
- **Gunicorn**
- **Nginx**
- **Git**
- **GitHub Actions**

Аутентификация пользователей реализована с помощью **токена**.

# Базовые модели проекта
### *Более подробно с базовыми моделями можно ознакомиться в спецификации API.*

- **Users**: пользователи.
- **Recipes**: рецепты.
- **Tags**: теги.
- **Ingredients**: ингредиенты.
- **Follow**: подписка на пользователей.
- **Shopping-cart**: список покупок.

# Пользовательские роли
- **Аноним**
- **Аутентифицированный пользователь**
- **Администратор**

# Запуск стека приложений с помощью docker-compose
Склонируйте репозиторий. 

В корневой директории создайте файл `.env` с переменными окружения для работы с базой данных:
```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Выполните команду `docker-compose up -d --build` для запуска сервера разработки.

Выполните миграции: `docker-compose exec web python manage.py migrate`.

Для заполнения базы ингредиентами (не обязательно) выполните команды:
```
docker-compose exec web python manage.py shell

# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

docker-compose exec web python manage.py load_data
```

Создайте суперпользователя: 

`docker-compose exec web python manage.py createsuperuser` 

Выполните _collectstatic_: 

`docker-compose exec web python manage.py collectstatic --noinput`.

Проект запущен и доступен по адресу [localhost](http://127.0.0.1/).


# OpenAPI
Документация API реализована с помощью ReDoc. Доступна по адресу [localhost/api/docs/](http://127.0.0.1/api/docs/).

# CI/CD
Для проекта Foodgram настроен _workflow_ со следующими инструкциями:
- автоматический запуск тестов (flake8)
- обновление образов на DockerHub
- автоматический деплой на боевой сервер при пуше в главную ветку master
