from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from .views import BookListView,BookCreateView,BookUpdateView,BookDeleteView
from django.contrib.auth.models import User
from .models import Book,Author
class BookListViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='john', password='big1234567')
        self.author = Author.objects.create(name='Test Author')
    def test_get_books(self):
        # Create a GET request
        request = self.factory.get('/books/')  # Use the URL path you have
        view = BookListView.as_view()
        response = view(request)
        
        # Check response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_books(self):
        #factory = APIRequestFactory
        request = self.factory.post('/books/create/',{'title':'new_idea','author': self.author.id,'publication_year':'2025'},format='json')
        
        force_authenticate(request, user=self.user)
        view = BookCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_books(self):
        book = Book.objects.create(
            title='new_idea',
            author=self.author,          # this is the Author object created in setUp
            publication_year=2025
        )
        book_id = book.id
        request = self.factory.put(f'books/update/{book_id}/',{'title':'updated_idea','author': self.author.id,'publication_year':'2025'},format='json')
        force_authenticate(request, user=self.user)
        view = BookUpdateView.as_view()
        response = view(request, pk=book_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_books(self):
        book = Book.objects.create(
        title='new_idea',
        author=self.author,
        publication_year=2025
        )
        book_id = book.id

        request = self.factory.delete(f'/books/delete/{book_id}/')
        force_authenticate(request, user=self.user)
        view = BookDeleteView.as_view()
        response = view(request, pk=book_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book_id).exists())
