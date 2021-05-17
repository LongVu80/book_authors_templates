from django.shortcuts import render, redirect
from .models import Books, Authors

def index(request):
    books = Books.objects.all()
    context = {
        "books": books
    }
    return render(request, 'index.html', context)

def createBook(request):
    if request.method == 'POST':
        Books.objects.create(
            title= request.POST['title'],
            desc= request.POST['description'],
        )
        return redirect('/')
    return redirect('/')

def showBook(request, bookId):
    thisBook = Books.objects.get(id= bookId)
    allAuthors = Authors.objects.all()

    context = {
        "thisBook": thisBook,
        "allAuthors": allAuthors,
    }
    return render(request,'showBook.html', context)

def addAuthor(request):
    bookId = request.POST['bookId']
    authorId = request.POST['authorId']
    thisBook = Books.objects.get(id=bookId)
    thisAuthor = Authors.objects.get(id=authorId)
    
    thisBook.authors.add(thisAuthor)
    return redirect(f"/book/{bookId}")

def newAuthor(request):
    authors = Authors.objects.all()
    context = {
        "authors": authors
    }
    return render(request, 'newAuthor.html', context)

def createAuthor(request):
    if request.method == 'POST':
        Authors.objects.create(
            first_name= request.POST['first_name'],
            last_name= request.POST['last_name'],
            notes= request.POST['notes'],
        )
        return redirect('/newAuthor')
    return redirect('/newAuthor')

def showAuthor(request, authorId):
    thisAuthor = Authors.objects.get(id=authorId)
    allBooks = Books.objects.all()

    context = {
        "thisAuthor": thisAuthor,
        "allBooks": allBooks,
    }
    return render(request, 'showAuthor.html', context)

def addBook(request):
    bookId = request.POST['bookId']
    authorId = request.POST['authorId']
    thisBook = Books.objects.get(id=bookId)
    thisAuthor = Authors.objects.get(id=authorId)
    
    thisAuthor.books.add(thisBook)
    return redirect(f"/author/{authorId}")


