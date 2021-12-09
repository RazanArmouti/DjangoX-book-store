from django.shortcuts import render
from .models import Books
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
)
# Create your views here.


class BooksListView(ListView):
    template_name = 'books/books_list.html'
    model = Books


class BooksDetailView(DetailView):
    template_name = 'books/books-details.html'
    model = Books
    context_object_name = 'books_detail'


class BooksCreateView(CreateView):
    template_name = 'books/create_books.html'
    model = Books
    fields = ['title', 'description', 'purchaser']


class BooksDeleteView(DeleteView):
    template_name = 'books/delete_books.html'
    model = Books
    success_url = reverse_lazy('bookstore')

class BooksUpdateView(UpdateView):
    template_name = 'books/update_book.html'
    model = Books
    fields = ['title', 'description']