from mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.ubicacion = db_data['ubicacion']
        self.idioma = db_data['idioma']
        self.comentario = db_data['comentario']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name, idioma, comentario, ubicacion, created_at , updated_at ) VALUES (%(name)s, %(idioma)s, %(comentario)s, %(ubicacion)s, NOW(),NOW());"
        return connectToMySQL('esquema_encuesta_dojo').query_db( query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        dojos= []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM dojos WHERE id = %i"%(id)
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        return cls(results[0])

    @staticmethod
    def validation(dojo):
        is_valid = True
        if len(dojo['name'])<3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['idioma'])<3:
            flash("Select a lenguage.")
            is_valid = False
        if len(dojo['ubicacion'])<3:
            flash("Select a location.")
            is_valid = False
        if len(dojo['comentario'])<3:
            flash("Write a comment.")
            is_valid = False
        return is_valid

