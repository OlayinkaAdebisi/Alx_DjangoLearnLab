from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework as filterz
# Create your views here.
# creates DRF views
class ListFilter(filterz.FilterSet):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')
class BookListView(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    # readonly for not authenticated
    #permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class =ListFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']
    search_fields = ['title','author__name']
    

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # readonly for not authenticated
    permission_classes = [IsAuthenticatedOrReadOnly]
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # provvides user authenitication and give crud
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    def get_queryset(self):
        return Book.objects.all()
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
