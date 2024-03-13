from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book, BookBorrow, User, Dept


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    time_publication = serializers.DateTimeField()
    count = serializers.IntegerField()
    
    dept_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    
    def validate(self, attrs):
        dept = Dept.objects.filter(pk=attrs['dept_id']).count()
        if dept == 0:
            raise ValidationError(detail='Department does not exist')
        
        return attrs
    
class DeptSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    
    def create(self, validated_data):
        return Dept.objects.create(**validated_data)
    
class UserSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class UserListSerializer(UserSerializer):
    num_books_borrowed = serializers.SerializerMethodField(read_only=True)
    def get_num_books_borrowed(self, obj):
        return obj.bookborrow_set.count()
    
class UserDetailSerializer(UserSerializer):
    books_on_hand  = serializers.SerializerMethodField(read_only=True)

    def get_books_on_hand(self, obj):
        book_borrows = obj.bookborrow_set.all()
        books = [book_borrow.book for book_borrow in book_borrows]
        return BookSerializer(books, many=True).data