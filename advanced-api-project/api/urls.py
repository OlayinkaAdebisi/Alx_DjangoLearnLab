from django.urls import path

from .views import BookListView,BookDetailView,BookCreateView,BookDeleteView,BookUpdateView
#handles the urls
urlpatterns=[
    path('books/',BookListView.as_view(),name='book_list'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='book_detail'),
    path('books/create/',BookCreateView.as_view(),name='book_create'),
    path('books/delete/',BookDeleteView.as_view(),name='book_delete'),
    path('books/update/',BookUpdateView.as_view(),name='book_update'),
]