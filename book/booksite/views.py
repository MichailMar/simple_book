from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import Book, BookBorrow, User, Dept
from .serializers import BookSerializer, UserSerializer, UserListSerializer, UserDetailSerializer, DeptSerializer
from .filtrers import BookFilter

from django_filters import rest_framework as filters

from django.db.models import Count
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filterset_class = BookFilter
    filter_backends = (filters.DjangoFilterBackend,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    action_serializers = {
        'retrieve': UserDetailSerializer,
        'list': UserListSerializer
    }

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def book_add(self, request, pk=None):
        book_id = request.data.get('book_id')  
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        if book.count <= 0:
            return Response({'error': 'No available copies of the book'}, status=status.HTTP_400_BAD_REQUEST)

        book.count -= 1
        book.save()
        
        user = self.get_object()
        
        BookBorrow.objects.create(
            user = user,
            book = book
        )

        return Response({'message': 'Book checked out successfully'})

    @action(detail=True, methods=['post'])
    def book_delete(self, request, pk=None):
        book_id = request.data.get('book_id') 
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            return Response({'error': 'User did not borrow this book'}, status=status.HTTP_400_BAD_REQUEST)

        book.count += 1
        book.save()

        user = self.get_object()

        BookBorrow.objects.filter(user=user, book=book).delete()
        
        return Response({'message': 'Book checked in successfully'})

class DeptViewSet(viewsets.ModelViewSet):
    
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    



def index(request: HttpRequest):
    
    id = request.GET.get("id")
    
    if not "user" in request.session:
        return redirect("auth")

    
    if id != None:
        user = User.objects.get(id=request.session['user'])
        book = Book.objects.get(id=int(id))
        
        BookBorrow.objects.create(user=user, book=book)
        return redirect("home")
    
    books = Book.objects.filter(count__gt=0).all()
    
    user_books = Book.objects.exclude(bookborrow__user=request.session["user"]).all()
    
    return render(request, "index.html", {"books": books, "user_books": user_books})

def auth(request: HttpRequest):
    
    if request.POST:
        name = request.POST.get("name")
        try:
            user = User.objects.get(name=name)
        except ObjectDoesNotExist:
            user = User.objects.create(name=name)

        request.session['user'] = user.id
        return redirect("home")
        
    if request.method == "GET":
        return render(request, "auth.html")