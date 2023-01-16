from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.friends = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO users ( first_name , last_name, created_at , updated_at ) VALUES (%(fname)s, %(lname)s,NOW(),NOW());"
        return connectToMySQL('amistades_esquema').query_db(query, data)
    
    @classmethod
    def add_friendship(cls, data):
        query= "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL('amistades_esquema').query_db(query, data)

    @classmethod
    def get_user_with_friends( cls , id ):
        query = ("SELECT * FROM users "+
                "JOIN friendships ON users.id = friendships.user_id "+
                "LEFT JOIN users AS friend ON friend.id = friendships.friend_id "+
                "WHERE users.id = %i;"%(id))
        results = connectToMySQL('amistades_esquema').query_db( query )
        user = cls( results[0] )
        for row_from_db in results:
            friends_data = {
                "id" : row_from_db["friend.id"],
                "first_name" : row_from_db["friend.first_name"],
                "last_name" : row_from_db["friend.last_name"],
                "created_at" : row_from_db["friend.created_at"],
                "updated_at" : row_from_db["friend.updated_at"]
            }
            user.friends.append( cls( friends_data ) )
        return user

    @classmethod
    def get_all_user_with_friends( cls ):
        query = ("SELECT * FROM users "+
                "JOIN friendships ON users.id = friendships.user_id "+
                "LEFT JOIN users AS friend ON friend.id = friendships.friend_id;")
        results = connectToMySQL('amistades_esquema').query_db( query )
        users = []
        for u in results:
            user = cls(u)
            friend_data = {
                "id" : u["friend.id"],
                "first_name" : u["friend.first_name"],
                "last_name" : u["friend.last_name"],
                "created_at" : u["friend.created_at"],
                "updated_at" : u["friend.updated_at"]
            }
            user.friends.append( cls( friend_data ) )
            users.append(user)
        return users

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_from_db =  connectToMySQL('amistades_esquema').query_db(query)
        users = []
        for user in users_from_db:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM users WHERE users.id = %i;"%(id)
        users_from_db = connectToMySQL('amistades_esquema').query_db(query)

        return cls(users_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('amistades_esquema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('amistades_esquema').query_db(query,data)