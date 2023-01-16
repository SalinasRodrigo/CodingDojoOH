from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Libro
from flask_app.models.author import Author


@app.route('/authors')
def index():
    return render_template("index.html", all_authors = Author.get_all())

@app.route('/books')
def books():
    return render_template("books.html", all_books = Libro.get_all())

@app.route('/authors/<int:author_id>')
def author_id(author_id):
    return render_template("author_des.html", author = Author.get_author_with_books(author_id),
                            all_books = Libro.get_all())

@app.route('/books/<int:book_id>')
def book_id(book_id):
    return render_template("book_des.html", book = Libro.get_books_with_authors(book_id),
                            all_authors = Author.get_all())

@app.route('/authors/process',methods=['POST'])
def create_author():
    data = {
        "fname":request.form['fname'],
        "lname":request.form['lname']
    }
    Author.save(data)
    return redirect('/authors')

@app.route('/books/process',methods=['POST'])
def create_book():
    data = {
        "title":request.form['title'],
        "num_page":request.form['num_page']
    }
    Libro.save(data)
    return redirect('/books')

@app.route('/authors/<int:author_id>/process',methods=['POST'])
def add_favorite_author(author_id):
    data = {
        "author_id": author_id,
        "book_id": request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect('/authors/'+str(author_id))

@app.route('/books/<int:book_id>/process',methods=['POST'])
def add_favorite_book(book_id):
    data = {
        "book_id": book_id,
        "author_id": request.form['author_id']
    }
    Author.add_favorite(data)
    return redirect('/books/'+str(book_id))
