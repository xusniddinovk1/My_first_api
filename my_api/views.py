from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer
from .models import Book


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
