from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookAddForm
from django.contrib import messages


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Book added successfully")
            return redirect('home')
    else:
        form = BookAddForm()
    return render(request, 'add_book.html', {'form': form})


def delete_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        messages.success(request, "Book deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
