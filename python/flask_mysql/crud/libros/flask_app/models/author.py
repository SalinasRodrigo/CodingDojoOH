from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.books = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( first_name , last_name, created_at , updated_at ) VALUES (%(fname)s, %(lname)s,NOW(),NOW());"
        return connectToMySQL('libros_esquema').query_db(query, data)
    
    @classmethod
    def add_favorite(cls, data):
        query= "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('libros_esquema').query_db(query, data)

    @classmethod
    def get_author_with_books( cls , id ):
        query = ("SELECT * FROM authors "+
                "LEFT JOIN  favorites ON authors.id = favorites.author_id "+
                "LEFT JOIN  books ON books.id = favorites.book_id "+
                "WHERE authors.id = %i;"%(id))
        results = connectToMySQL('libros_esquema').query_db( query)
        author = cls( results[0] )
        for row_from_db in results:
            books_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_page" : row_from_db["num_page"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.books.append( book.Libro( books_data ) )
        return author

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors_from_db =  connectToMySQL('libros_esquema').query_db(query)
        authors = []
        for author in authors_from_db:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM authors WHERE authors.id = %i;"%(id)
        dojos_from_db = connectToMySQL('libros_esquema').query_db(query)

        return cls(dojos_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE authors SET first_name=%(fname)s, last_name=%(lname)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('libros_esquema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL('libros_esquema').query_db(query,data)