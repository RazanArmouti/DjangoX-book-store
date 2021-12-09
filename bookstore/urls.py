from django.urls import path
from .views import (BooksListView, BooksDetailView,
                    BooksCreateView, BooksDeleteView,
                     BooksUpdateView)


urlpatterns = [
    path('' ,BooksListView.as_view(), name='bookstore'),
    path('<int:pk>/' ,BooksDetailView.as_view(), name='books-details'),
    path('create/' ,BooksCreateView.as_view(), name='create_books'),
    path('<int:pk>/update/' ,BooksUpdateView.as_view(), name='update_books'),
    path('/delete/<int:pk>' ,BooksDeleteView.as_view(), name='delete_books'),
]