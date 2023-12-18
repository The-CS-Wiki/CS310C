#
#  Author: Benjamin Herrera
#

# Imports
from pymongo import MongoClient
from flask import Blueprint

# Connect to the local MongoDB server
CLIENT = MongoClient("localhost", 27017)

# Practice 1 BPs
movies = Blueprint("movies", __name__)


@movies.route("/movies", methods=["GET"])
def movies_endpoint():
    return {"movies": ["The Green Knight", "Star Trek", "Godzilla"]}, 200


def setup(data):
    """Sets up the practice file"""
    # Focus on the DB and collection
    db = CLIENT["practice_db"]
    col = db["practice_collection"]

    # Seed the database with given data
    col.insert_many(data)


def drop():
    CLIENT.drop_database("practice_db")
    CLIENT.close()
