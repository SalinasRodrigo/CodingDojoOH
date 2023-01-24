from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])\S{8,16}$')
from flask import flash

class Ususario:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido'] 
        self.email = db_data['email']
        self.contraseña = db_data['contraseña']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO usuarios ( nombre, apellido, email, contraseña, created_at , updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contraseña)s, NOW(),NOW());"
        result = connectToMySQL('inicio_registro_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        emails_from_db =  connectToMySQL('inicio_registro_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id = %(user_id)s;"
        result = connectToMySQL('inicio_registro_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL('inicio_registro_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s,  email=%(email)s, contraseña=%(contraseña)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('inicio_registro_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM usuarios WHERE id = %i;"%(id)
        return connectToMySQL('inicio_registro_db').query_db(query)

    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  ( not data['nombre'].isalpha() or len(data['nombre'])<3):
            flash('El nombre debe tener al menos 3 caracteres y no debe contener caracteres numericos.', 'registro')
            is_true = False
        if  ( not data['apellido'].isalpha() or len(data['apellido'])<3):
            flash('El apellido debe tener al menos 3 caracteres y no debe contener caracteres numericos.', 'registro')
            is_true = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Formato de email incorrecto.', 'registro')
            is_true = False
        if  Ususario.get_by_email(data):
            flash('Ya existe un ususario registrado con ese correo.', 'registro')
            is_true = False
        if not PASSWORD_REGEX.match(data['contraseña']):
            flash('La contraseña debe terner almenos un numero y una letra mayuscula.', 'registro')
            is_true = False
        if len(data['contraseña'])<8:
            flash('La contraseña debe tener almenos 8 caracteres', 'registro')
            is_true = False
        if not data['contraseña'] == data['confirmacion']:
            flash ('Las contraseñas no coinciden', 'registro')
            is_true = False
        return is_true

    # @staticmethod
    # def validacion_login(data):
    #     is_true = True
    #     if not Ususario.get_by_email(data['email']):

    