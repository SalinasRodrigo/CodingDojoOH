from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import like

class Thought:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.contents = db_data['contents']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None
        self.likes = 0

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO thoughts ( contents, user_id, created_at , updated_at) " + 
                "VALUES (%(contents)s, %(user_id)s, NOW(), NOW());")
        result = connectToMySQL('thought_db').query_db(query, data)
        return result

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        return connectToMySQL('thought_db').query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE thoughts SET contents=%(contents)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('thought_db').query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM thoughts WHERE id = %(id)s;"
        print(query)
        results =  connectToMySQL('thought_db').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_one_user_thoughts(cls, data):
        query = ("SELECT * FROM thoughts "+
                "LEFT JOIN users ON users.id = thoughts.user_id "+
                "WHERE thoughts.id = %(tought_id)s;")
        results =  connectToMySQL('thought_db').query_db(query, data)
        
        if not results:
            return results
        
        user_data = {
            "id" : results[0]["users.id"],
            "first_name" : results[0]["first_name"],
            "last_name" : results[0]["last_name"],
            "password" : results[0]["password"],
            "email" : results[0]["email"],
            "created_at" : results[0]["users.created_at"],
            "updated_at" : results[0]["users.updated_at"]
        }
        thought = cls(results[0])
        thought.user = user.User(user_data)
        return thought


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM thoughts;"
        results =  connectToMySQL('thought_db').query_db(query)
        thoughts = []
        for recipe in results:
            thoughts.append(cls(recipe))
        return thoughts

    @classmethod
    def get_all_user_thoughts(cls):
        query = ("SELECT * FROM thoughts "+
                "LEFT JOIN users ON users.id = thoughts.user_id;")
        results =  connectToMySQL('thought_db').query_db(query)
        thoughts = []
        if not results:
            return results
        for row_db in results:
            user_data = {
                "id" : row_db["users.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "password" : row_db["password"],
                "email" : row_db["email"],
                "created_at" : row_db["users.created_at"],
                "updated_at" : row_db["users.updated_at"]
            }

            thought = cls(row_db)
            thought.user = user.User(user_data)
            thoughts.append(thought)
            data = {
                "id": thought.id
            }
            thought.likes = like.Like.get_likes_num(data)
        return thoughts

    def liked(self, likes):
        for like in likes:
            if like.user_id == self.user_id and like.thought_id == self.id:
                return True
        return False

    