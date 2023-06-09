from django.shortcuts import render
from .models import *
from django.views import generic
from django.db.models import Q


# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    contecontext_object_name = 'book_list'
    def get_queryset(self):
        query = self.request.GET.get("q") if self.request.GET.get("q") != None else ""
        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
    template_name = 'catalog/books.html'

class AuthorListView(generic.ListView):
    model = Author
    contecontext_object_name = 'author_list'
    def get_queryset(self):
        query = self.request.GET.get("q") if self.request.GET.get("q") != None else ""
        object_list = Author.objects.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)
        )
        return object_list
    template_name = 'catalog/authors.html'

class GenreListView(generic.ListView):
    model = Genre
    contecontext_object_name = 'genre_list'
    def get_queryset(self):
        query = self.request.GET.get("q") if self.request.GET.get("q") != None else ""
        object_list = Genre.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
    template_name = 'catalog/genres.html'

# BACKUP: in case I get tired of learning CBVs:
# def books(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render (request,'catalog/books.html' ,context=context)
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book-detail.html'
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author-detail.html'

