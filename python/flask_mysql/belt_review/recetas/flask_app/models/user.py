from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])\S{8,16}$')
from flask import flash

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name'] 
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at , updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(),NOW());"
        result = connectToMySQL('recetas_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        emails_from_db =  connectToMySQL('recetas_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL('recetas_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recetas_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s,  email=%(email)s, password=%(password)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('recetas_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM users WHERE id = %i;"%(id)
        return connectToMySQL('recetas_db').query_db(query)


    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  ( not data['fname'].isalpha() or len(data['fname'])<3):
            flash('El first_name debe tener al menos 3 caracteres y no debe contener caracteres numericos.', 'registro')
            is_true = False
        if  ( not data['lname'].isalpha() or len(data['lname'])<3):
            flash('El last_name debe tener al menos 3 caracteres y no debe contener caracteres numericos.', 'registro')
            is_true = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Formato de email incorrecto.', 'registro')
            is_true = False
        if  User.get_by_email(data):
            flash('Ya existe un ususario registrado con ese correo.', 'registro')
            is_true = False
        if not PASSWORD_REGEX.match(data['password']):
            flash('La password debe terner almenos un numero y una letra mayuscula.', 'registro')
            is_true = False
        if len(data['password'])<8:
            flash('La password debe tener almenos 8 caracteres', 'registro')
            is_true = False
        if not data['password'] == data['confi']:
            flash ('Las passwords no coinciden', 'registro')
            is_true = False
        return is_true

    # @staticmethod
    # def validacion_login(data):
    #     is_true = True
    #     if not Ususario.get_by_email(data['email']):

    