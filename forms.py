from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class CupcakeForm(FlaskForm):
    """ Form to add new cupcakes """

    c_flavor = StringField("Cupcake Flavor:")
    c_size = StringField("Cupcake Size: ")
    c_rating = FloatField("Cupcake Rating: ")
    c_image = StringField("Cupacake Image: ")