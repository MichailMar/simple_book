from django.db.models import Model
from django.db.models import TextField, DateTimeField, IntegerField, ForeignKey, CASCADE, CharField, PositiveIntegerField

    
class Dept(Model):
    """
    Модель таблицы  с отделами библиотеки
    """
    name = TextField("Название отдела") 

    def __str__(self):
        return self.name

class Book(Model):
    """
    Модель таблицы с книгами
    """
    titile = CharField("Название книги", blank=True)
    author = CharField("Автор книги" ,blank=True)
    time_publication = DateTimeField("Дата публикации")
    count = PositiveIntegerField("Кол-во экземпляров", default=0)
    
    dept = ForeignKey("Dept", on_delete=CASCADE)
    
    def __str__(self):
        return self.titile

class User(Model):
    """
    Модель таблицы с информацией о пользователе
    """
    name = CharField("Имя пользователя")
    
    def __str__(self):
        return self.name
    
class BookBorrow(Model):
    """
    Модель таблицы с данными о взятых книгах пользователем
    """
    user = ForeignKey(User, on_delete=CASCADE)
    book = ForeignKey(Book, on_delete=CASCADE)
    
