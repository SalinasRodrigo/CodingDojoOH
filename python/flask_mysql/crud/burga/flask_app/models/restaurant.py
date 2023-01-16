from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger
class Restaurant:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un restaurante
        self.burgers = []
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO restaurants ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('restaurant_db').query_db( query, data)
    
    @classmethod
    def get_restaurant_with_burgers( cls , data ):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        results = connectToMySQL('restaurant_db').query_db( query , data )
        # los resultados serán una lista de objetos topping (aderezo) con la hamburguesa adjunta a cada fila 
        restaurant = cls( results[0] )
        for row_from_db in results:
            # ahora parseamos los datos de hamburguesa para crear instancias de hamburguesa y agregarlas a nuestra lista
            burger_data = {
                "id" : row_from_db["burgers.id"],
                "name" : row_from_db["burgers.name"],
                "bun" : row_from_db["bun"],
                "meat" : row_from_db["meat"],
                "calories" : row_from_db["calories"],
                "created_at" : row_from_db["burgers..created_at"],
                "updated_at" : row_from_db["burgers.updated_at"]
            }
            restaurant.burgers.append( burger.Burger( burger_data ) )
        return restaurant

    @classmethod
    def get_all_restaurant(cls):
        query = "SELECT * FROM restaurants"
        results = connectToMySQL('restaurant_db').query_db(query)
        restaurants = []
        for b in results:
            restaurants.append(cls(b))
        return restaurants