from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .serializers import BookSerializer, UsersSerializer
from .models import Book 
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model



# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailAPIBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CrudAPIBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly)

class CreateAPIBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly)



class UsersAPIList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer

class UsersAPIDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer




