from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Book

# Vista principal: lista de libros
def home(request):
    # Obtiene todos los libros de la base de datos
    books = Book.objects.all()
    # Envía la lista a la plantilla como contexto
    return render(request, 'books/home.html', {'books': books})

# Vista de detalle: un libro por id
def detail_book(request, book_id):
    # Busca el libro por su id, si no existe devuelve error 404
    book = get_object_or_404(Book, id=book_id)
    # Envía el libro a la plantilla como contexto
    return render(request, 'books/detail_book.html', {'detail_book': book})
