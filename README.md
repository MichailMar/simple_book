# simple_book
 
# Инструкция по установке

поднимите докер контейнер
docker-compose up -d
выполните мигарции 
docker-compose exec site python manage.py makemigrations 
docker-compose exec site python manage.py migrate
Всё готово к использованию
