from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    recipe = db.Column(db.String)
    pantry = db.Column(db.String)
    grocery_list = db.Column(db.String)

    def  __init__(self, recipe, pantry, grocery_list ):
        self.recipe = recipe
        self.pantry = pantry
        self.grocery_list = grocery_list


class UserSchema(ma.Schema):
    class Meta: 
        fields = ('username', 'password')

class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('recipe', 'pantry', 'grocery_list')

recipe_schema = RecipeSchema()
multi_recipe_schema = RecipeSchema(many=True)

user_schema = UserSchema()

