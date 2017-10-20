from flask import Flask, jsonify, render_template
import numpy as np
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Grab connection URL from local environment variables
connection_var = os.environ.get("mysql_connection1")
engine = create_engine(connection_var)

# Uses local config file
# from config import connection
# connection_string = connection["mysql_connection"]
# print(connection_string)
# engine = create_engine(connection_string)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
IceCreamFlavors = Base.classes.icecreamstore
# Avengers = Base.classes.avengers

# Create our session (link) from Python to the DB
session = Session(engine)

# results = session.query(IceCreamFlavors).all()
# # Convert list of tuples into normal list
# all_flavors = []
# for flavor in results:
#     print(flavor.Flavors)
#     print(flavor.Quantities)
#     print(flavor.Price)
#     flavor_dict = {}
#     flavor_dict["flavor"] = flavor.Flavors
#     flavor_dict["quantities"] = float(flavor.Quantities)
#     flavor_dict["price"] = float(flavor.Price)
#     all_flavors.append(flavor_dict)

# print(all_flavors)

# Flask setup
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    print("Retrieving homepage")
    return "Welcome to my hompage"

@app.route("/api/ice_cream_flavors")
def all_justice():
    """Return a list of all ice-cream flavors"""
    print("Retrieving ice_cream_flavors API")
    # Query all passengers
    results = session.query(IceCreamFlavors).all()
    # Convert list of tuples into normal list
    all_flavors = []
    for flavor in results:
        flavor_dict = {}
        flavor_dict["flavor"] = flavor.Flavors
        flavor_dict["quantities"] = float(flavor.Quantities)
        flavor_dict["price"] = float(flavor.Price)
        all_flavors.append(flavor_dict)

    return jsonify(all_flavors)

# @app.route("/api/avengers")
# def all_avengers():
#     """Return a list of all passenger names"""
#     print("Retrieving avengers API")
#     # Query all passengers
#     Avengers = Base.classes.avengers
#     results = session.query(Avengers).all()

#     # Convert list of tuples into normal list
#     all_superheros = []
#     for superhero in results:
#         superhero_dict = {}
#         superhero_dict["superhero"] = superhero.superhero
#         superhero_dict["real_name"] = superhero.real_name
#         all_superheros.append(superhero_dict)

#     return jsonify(all_superheros)


if __name__ == '__main__':
    app.run(debug=False)
