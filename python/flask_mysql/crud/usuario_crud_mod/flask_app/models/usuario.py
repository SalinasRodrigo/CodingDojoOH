# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuario_db').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usurario in results:
            usuarios.append( cls(usurario) )
        return usuarios

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id=%i;"% (id)
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        usuario = connectToMySQL('usuario_db').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        
        return cls(usuario[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuario_db').query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE usuarios SET first_name = %(fname)s , last_name = %(lname)s , email= %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('usuario_db').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id=%i;"%(id)
        return connectToMySQL('usuario_db').query_db(query)