from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Book, Comment
from .forms import CommentForm


class BookListView(generic.ListView):
    model= Book
    paginate_by= 4
    template_name= 'books/book_list.html'
    context_object_name= 'books'

    def get_queryset(self):
        return Book.objects.all()



# class BookDetailView(generic.DetailView):
#     model= Book
#     template_name= 'books/book_detail.html'
#     context_object_name= 'book'


@login_required
def book_detail_view(request, pk):
    book= get_object_or_404(Book, pk=pk)

    book_comment= book.comments.all().order_by('-datetime_created')

    if request.method == "POST":
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.book= book
            new_comment.user= request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book, 
        "comments": book_comment,
        "form": comment_form,
        })



class BookCreateView(LoginRequiredMixin ,generic.CreateView):
    model= Book
    template_name= 'books/book_create.html'
    fields= ['title' ,'description' ,'author' ,'price', 'cover']
    


class BookUpdateView(LoginRequiredMixin ,UserPassesTestMixin ,generic.UpdateView):
    model= Book
    template_name= 'books/book_update.html'
    fields= ['title' ,'description' ,'author' ,'price', 'cover']

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    

class BookDeleteView(LoginRequiredMixin ,UserPassesTestMixin ,generic.DeleteView):
    model= Book
    template_name= 'books/book_delete.html'
    success_url= reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    


