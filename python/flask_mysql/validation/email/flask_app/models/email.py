from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash

class Email:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO emails ( email, created_at , updated_at ) VALUES (%(email)s, NOW(),NOW());"
        return connectToMySQL('email_db').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        emails_from_db =  connectToMySQL('email_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM emails WHERE id = %i;"%(id)
        emails_from_db = connectToMySQL('email_db').query_db(query)

        return cls(emails_from_db[0])

    @classmethod
    def get_by_name(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        result = connectToMySQL('email_db').query_db(query, data)

        return result

    @classmethod
    def update(cls,data):
        query = "UPDATE emails SET email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('email_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM emails WHERE id = %i;"%(id)
        return connectToMySQL('email_db').query_db(query)

    @staticmethod
    def validacion(user):
        is_valid=True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if Email.get_by_name(user):
            flash("This email already exists")
            is_valid = False
        return is_valid


    