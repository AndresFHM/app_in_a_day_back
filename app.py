from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)



class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idMeal = db.Column(db.String(100), unique=False)
    strMeal = db.Column(db.String(144), unique=False)
    strMealThumb = db.Column(db.String(100), unique=False)

    def __init__(self, idMeal, strMeal, strMealThumb):
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strMealThumb = strMealThumb
        


class GuideSchema(ma.Schema):
    class Meta:
        fields = ('idMeal', 'strMeal', 'strMealThumb')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

# Endpoint to create a new guide
@app.route('/recipe', methods=["POST"])
def add_guide():
    idMeal = request.json['idMeal']
    strMeal = request.json['strMeal']
    strMealThumb = request.json['strMealThumb']

    new_guide = Guide(idMeal, strMeal, strMealThumb)

    db.session.add(new_guide)
    db.session.commit()

    guide = Guide.query.get(new_guide.id)

    return guide_schema.jsonify(guide)


# Endpoint to query all guides
@app.route("/recipes", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)


# Endpoint for querying a single guide
@app.route("/recipe/<id>", methods=["GET"])
def get_guide(id):
    guide = Guide.query.get(id)
    return guide_schema.jsonify(guide)


# Endpoint for updating a guide
@app.route("/recipe/<id>", methods=["PUT"])
def guide_update(id):
    guide = Guide.query.get(id)
    idMeal = request.json['idMeal']
    strMeal = request.json['strMeal']
    strMealThumb = request.json['strMealThumb']

    new_guide = Guide(idMeal, strMeal, strMealThumb)

    db.session.commit()
    return guide_schema.jsonify(guide)

# Endpoint for deleting a record
@app.route("/recipe/<id>", methods=["DELETE"])
def guide_delete(id):
    guide= Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()

    return "guide was successfully deleted"



if __name__ == '__main__':
    app.run(debug=True)


