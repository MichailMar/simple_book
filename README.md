# simple_book
 
# Инструкция по установке

1. поднимите докер контейнер
  * docker-compose up -d
2. выполните мигарции 
  * docker-compose exec site python manage.py makemigrations 
  * docker-compose exec site python manage.py migrate
3. Всё готово к использованию. Сайт запускается на localhost:80
