from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model= Book
    template_name= 'books/book_list.html'
    context_object_name= 'books'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.all()



class BookDetailView(generic.DetailView):
    model= Book
    template_name= 'books/book_detail.html'
    context_object_name= 'book'



class BookCreateView(generic.CreateView):
    model= Book
    template_name= 'books/book_create.html'
    fields= ['title' ,'description' ,'author' ,'price']
    


class BookUpdateView(generic.UpdateView):
    model= Book
    template_name= 'books/book_update.html'
    fields= ['title' ,'description' ,'author' ,'price']



class BookDeleteView(generic.DeleteView):
    model= Book
    template_name= 'books/book_delete.html'
    success_url= reverse_lazy('book_list')