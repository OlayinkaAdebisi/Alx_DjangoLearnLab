from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
# Create your views here.
# creates DRF views
class BookListView(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    # readonly for not authenticated
    #permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['title', 'author', 'publication_year']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title ']


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
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
class BookDeleteView(generics.DestroyAPIView):
    queryset = BookSerializer
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
