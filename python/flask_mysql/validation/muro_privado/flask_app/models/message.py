from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from datetime import datetime
import math

class Message:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.message = db_data['message']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.remitent_id = db_data['remitent_id']
        self.destinatary_id = db_data['destinatary_id']
        self.remitent = None

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO messages ( message, remitent_id, destinatary_id, created_at , updated_at) VALUES (%(message)s, %(remitent_id)s, %(destinatary_id)s, NOW(), NOW());"
        result = connectToMySQL('muro_privado_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM messages WHERE id = %i;"%(id)
        return connectToMySQL('muro_privado_db').query_db(query)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages;"
        results =  connectToMySQL('muro_privado_db').query_db(query)
        messages = []
        for mesagge in results:
            messages.append(cls(mesagge))
        return messages

    @classmethod
    def get_by_destinatary(cls, data):
        query = ("SELECT * FROM messages " +
                "LEFT JOIN users ON users.id = messages.remitent_id " +
                "WHERE messages.destinatary_id = %(user_id)s "+
                "ORDER BY first_name ASC;")
        results =  connectToMySQL('muro_privado_db').query_db(query, data)
        messages = []
        if not results:
            return results
 
        for row_db in results:
            remitent_data = {
                "id" : row_db["users.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "password" : row_db["password"],
                "email" : row_db["email"],
                "created_at" : row_db["users.created_at"],
                "updated_at" : row_db["users.updated_at"]
            }
            message = cls(row_db)
            message.remitent = user.User(remitent_data)
            messages.append(message)
        return messages

    @classmethod
    def get_num_messages(cls, data):
        query = ("SELECT count(*) as num FROM messages "+
                "LEFT JOIN users ON users.id = messages.remitent_id "+
                "where messages.destinatary_id=%(user_id)s "+
                "group by destinatary_id;")
        results =  connectToMySQL('muro_privado_db').query_db(query, data)
        if not results:
            return 0 
        return results[0]['num']
    
    @classmethod
    def get_num_send(cls, data):
        query = ("SELECT count(*) as num FROM messages "+
                "LEFT JOIN users ON users.id = messages.destinatary_id "+
                "where messages.remitent_id=%(user_id)s "+
                "group by destinatary_id;")
        results =  connectToMySQL('muro_privado_db').query_db(query, data)
        if not results:
            return 0 
        return results[0]['num']

    def time_span(slef):
        ahora = datetime.now()
        result = ahora - slef.created_at
        if result.days > 0:
            return f"{result.days} days ago"
        elif (math.floor(result.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(result.total_seconds() / 60)/60)} hours ago"
        elif result.total_seconds() >= 60:
            return f"{math.floor(result.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(result.total_seconds())} seconds ago"