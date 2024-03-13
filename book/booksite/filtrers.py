import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    available = django_filters.BooleanFilter(method='filter_available')

    class Meta:
        model = Book
        fields = '__all__'

    def filter_available(self, queryset, name, value):
        if value:
            return queryset.filter(count__gt=0)
        else:
            return queryset.filter(count=0)