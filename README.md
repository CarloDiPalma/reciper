# praktikum_new_diplom
# Foodgram
Cервис для публикаций и обмена рецептами.

Авторизованные пользователи могут подписываться на понравившихся авторов, добавлять рецепты в избранное, в покупки, скачивать список покупок. Неавторизованным пользователям доступна регистрация, авторизация, просмотр рецептов других пользователей.

![Foodgram Workflow](https://github.com/CarloDiPalma/foodgram-project-react/actions/workflows/main.yml/badge.svg)


## Стек технологий
Python 3.9.10, Django 3.2.20, Django REST Framework 3.14, PostgresQL, Docker, Yandex.Cloud.

## Установка
Для запуска локально, создайте файл `.env` в корневой директории с содержанием:
```
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
POSTGRES_DB=foodgram_db
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_ENGINE=django.db.backends.postgresql
DB_NAME=foodgram_db
DB_HOST=localhost
DB_PORT=5432
```
В соответствии с этими параметрами также необходимо настроить БД Postgres на вашем локальном ПК.
#### Установка Docker
Для запуска проекта вам потребуется установить Docker и docker-compose.

Для установки на ubuntu выполните следующие команды:
```bash
sudo apt install docker docker-compose
```

Про установку на других операционных системах вы можете прочитать в [документации](https://docs.docker.com/engine/install/) и [про установку docker-compose](https://docs.docker.com/compose/install/).

### Установка проекта на сервер
1. Скопируйте файлы из папки `/server/` на ваш сервер и `.env` файл из директории `/backend/`:
```bash
scp -r data/ <username>@<server_ip>:/home/<username>/
scp backend/.env <username>@<server_ip>:/home/<username>/
```
2. Зайдите на сервер и настройте `server_name` в конфиге nginx на ваше доменное имя:
```bash
vim nginx.conf
```

### Настройка проекта
1. Запустите docker compose:
```bash
docker-compose up -d
```
2. Примените миграции:
```bash
docker-compose exec backend python manage.py migrate
```
3. Заполните базу начальными данными (необязательно):
```bash
docker-compose exec backend python manange.py load_ingredients
```
4. Создайте администратора:
```bash
docker-compose exec backend python manage.py createsuperuser
```
5. Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic
```





## Документация к API
Чтобы открыть документацию локально, запустите сервер и перейдите по ссылке:
[http://127.0.0.1/api/docs/](http://127.0.0.1/api/docs/)