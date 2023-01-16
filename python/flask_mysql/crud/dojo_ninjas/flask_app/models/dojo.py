from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # Creamos una lista para que luego podamos agregar todas los ninjas que están asociadas a un dojo
        self.ninjas = []
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_db').query_db( query, data)
    
    @classmethod
    def get_dojo_with_ninjas( cls , id ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %i;"%(id)
        results = connectToMySQL('dojos_db').query_db( query)
        print(results)
        dojo = cls( results[0] )
        for row_from_db in results:
            # ahora parseamos los datos de hamburguesa para crear instancias de hamburguesa y agregarlas a nuestra lista
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo

    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_db').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos