from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Libro:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.title = db_data['title']
        self.num_page = db_data['num_page']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # Creamos una lista para que luego podamos agregar todas los author que están asociadas a un books
        self.favorite_by = []
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO books ( title, num_page, created_at , updated_at ) VALUES (%(title)s, %(num_page)s,NOW(),NOW());"
        return connectToMySQL('libros_esquema').query_db( query, data)
    
    @classmethod
    def get_books_with_authors( cls , id ):
        query = ("SELECT * FROM books "+
                "LEFT JOIN  favorites ON books.id = favorites.book_id "+
                "LEFT JOIN  authors ON authors.id = favorites.author_id "+
                "WHERE books.id = %i;"%(id))
        results = connectToMySQL('libros_esquema').query_db( query)
        book = cls( results[0] )
        for row_from_db in results:
            # ahora parseamos los datos de hamburguesa para crear instancias de hamburguesa y agregarlas a nuestra lista
            author_data = {
                "id" : row_from_db["authors.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.favorite_by.append( author.Author( author_data ) )
        return book

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('libros_esquema').query_db(query)
        books= []
        for book in results:
            books.append(cls(book))
        return books