from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import thought
from flask_app.models import user

class Like:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.thought_id = db_data['thought_id'] 
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO likes ( thought_id, user_id, created_at , updated_at) " + 
                "VALUES (%(thought_id)s, %(user_id)s, NOW(), NOW());")
        result = connectToMySQL('thought_db').query_db(query, data)
        return result

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM likes WHERE thought_id = %(thought_id)s and user_id = %(user_id)s ;"
        return connectToMySQL('thought_db').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM likes;"
        results = connectToMySQL('thought_db').query_db(query)
        likes = []
        for like in results:
            likes.append(cls(like))
        return likes

    @classmethod
    def get_likes_num(cls, data):
        query = ("SELECT count(*) as num FROM thoughts "+
                "JOIN likes ON thoughts.id = likes.thought_id "+
                "where thoughts.id = %(id)s "+
                "order by likes.id;")
        result = connectToMySQL('thought_db').query_db(query, data)
        if not result:
            return 0
        return int(result[0]['num'])