# simple_book

# Инструкция по установке
Таймауты меняются в nginx.conf, настройки для базы в json не делал, т.к. у нас она в контейнере
1. поднимите докер контейнер
  * docker-compose up -d
2. выполните мигарции 
  * docker-compose exec site python manage.py makemigrations 
  * docker-compose exec site python manage.py migrate
3. Всё готово к использованию. Сайт запускается на localhost:80

# Эндпоинты
1. / - главная страница с книгами
2. /auth - авторизация/регистрация
3. /api/v1/users (get) - список всех пользователей, (post) - создать пользователя. Пример json {"name": "Михаил}
4. /api/v1/users/<id> (get) - детальная информация о пользователе, (delete) удалить пользователя
5. /api/v1/users/<id>/book_add (post)- выдать книгу. Пример json {'book_id': 4}
6. /api/v1/users/<id>/book_delete (post) забрать книгу. Пример json {'book_id': 4}
7. /api/v1/books (get) - список всех книг + фильтры в url (title, author, time_publication, dept, available), (post) - создать кингу. Пример json {"title":"Евгений Онегин","author":"Пушкин","time_publication":"1833-12-12T12:45:00Z","count":10,"dept_id":1}
8. /api/v1/departaments (get) - список всех отделов, (post) - создать отдел. Пример json {"name": "Михаил"}
