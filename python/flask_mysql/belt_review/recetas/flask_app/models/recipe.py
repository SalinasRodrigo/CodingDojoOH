from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from datetime import datetime
import math

class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instruction = db_data['instruction']
        self.time = db_data['time']
        self.date = db_data['date']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO recipes ( name, description, instruction, time, date, user_id, created_at , updated_at) " + 
                "VALUES (%(name)s, %(description)s, %(instruction)s, %(time)s, %(date)s, %(user_id)s, NOW(), NOW());")
        result = connectToMySQL('recetas_db').query_db(query, data)
        return result

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recetas_db').query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s,  instruction=%(instruction)s, time=%(time)s, date=%(date)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('recetas_db').query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        print(query)
        results =  connectToMySQL('recetas_db').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_one_user_recipes(cls, data):
        query = ("SELECT * FROM recipes "+
                "LEFT JOIN users ON users.id = recipes.user_id "+
                "WHERE recipes.id = %(recipe_id)s;")
        results =  connectToMySQL('recetas_db').query_db(query, data)
        
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
        recipe = cls(results[0])
        recipe.user = user.User(user_data)
        return recipe


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL('recetas_db').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_all_user_recipes(cls):
        query = ("SELECT * FROM recipes "+
                "LEFT JOIN users ON users.id = recipes.user_id;")
        results =  connectToMySQL('recetas_db').query_db(query)
        recipes = []
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
            recipe = cls(row_db)
            recipe.user = user.User(user_data)
            recipes.append(recipe)
        return recipes

    def date_format(self):
        formato = self.date.strftime("%B") + " "+ self.date.strftime("%d") + "," + self.date.strftime("%Y")
        return formato
    
    @staticmethod
    def validation(data):
        is_true = True
        if len(data['name'])<3:
            is_true = False
            flash('Name must be have 3 characters.', 'recipe')
        if len(data['description'])<3:
            is_true = False
            flash('Description must be have 3 characters.', 'recipe')
        if len(data['instruction'])<3:
            is_true = False
            flash('Instruction must be have 3 characters.', 'recipe')
        if not data['date']:
            is_true = False
            flash('Date is required.', 'recipe')
        if not data['time']:
            is_true= False
            flash('Do you recipe take less than 30 minutes?', 'recipe')
        return is_true