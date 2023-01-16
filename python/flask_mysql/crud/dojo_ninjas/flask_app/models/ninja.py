from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojo_id, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s,NOW(),NOW());"
        return connectToMySQL('dojos_db').query_db(query,data)
 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL('dojos_db').query_db(query)
        ninjas =[]
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        dojos_from_db = connectToMySQL('dojos_db').query_db(query,data)

        return cls(dojos_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s, dojo_id=%(dojo_id)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_db').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_db').query_db(query,data)