# simple_book

# Инструкция по установке
Таймауты меняются в nginx.conf, настройки для базы в json не делал, т.к. у нас она в контейнере
1. поднимите докер контейнер
  * docker-compose up -d
2. выполните мигарции 
  * docker-compose exec site python manage.py makemigrations 
  * docker-compose exec site python manage.py migrate
3. Всё готово к использованию. Сайт запускается на localhost:80
