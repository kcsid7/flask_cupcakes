"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, redirect

from models import db, connect_db, Cupcake
from forms import CupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "alksdfjlkasjdlksadfjaasdf"

connect_db(app)


@app.route("/")
def root_route():
    """ Root Route """

    form = CupcakeForm()

    return render_template("index.html", form=form)


@app.route("/api/cupcakes")
def all_cupcakes():
    """ Get data about all cupcakes. Respond with JSON : {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    data = [ cupcake.get_info() for cupcake in Cupcake.query.all() ]
    return jsonify(cupcakes = data)

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """ Add new cupcake. Get JSON data in the form: { flavor: "", size: "", rating: "", image: ""} """
    new_cupcake = Cupcake(
        flavor = request.json["flavor"],
        size = request.json["size"],
        rating = request.json["rating"],
        image = request.json["image"] or None,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake = new_cupcake.get_info()), 201)



@app.route("/api/cupcakes/<int:cupcake_id>")
def one_cupcake(cupcake_id):
    """ Get more info about the cupcake """
    data = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcakes = data.get_info())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ Patch/Update a cupcake entry"""


    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]

    db.session.add(cupcake)
    db.session.commit()

    return jsonify( cupcakes = cupcake.get_info())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ Delete selected cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Deleted!"
    })


