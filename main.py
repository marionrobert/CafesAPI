from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    if request.method == "GET":
        all_cafes = Cafe.query.all()
        random_cafe = random.choice(all_cafes)
        # return jsonify(cafe={
        #     "can_take_calls": random_cafe.can_take_calls,
        #     "coffee_price": random_cafe.coffee_price,
        #     "has_sockets": random_cafe.has_sockets,
        #     "has_toilet": random_cafe.has_toilet,
        #     "has_wifi": random_cafe.has_wifi,
        #     "id": random_cafe.id,
        #     "img_url": random_cafe.img_url,
        #     "location": random_cafe.location,
        #     "map_url": random_cafe.map_url,
        #     "name": random_cafe.name,
        #     "seats": random_cafe.seats
        # })
        return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    all_cafes = [cafe.to_dict() for cafe in Cafe.query.all()]
    return jsonify(cafes=all_cafes)


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
