#
#  Author: Benjamin Herrera
#
#  CS310C // API Server with Flask
#  Chapter 1: Endpoints
#

""" You are tasked to complete the TODO's of this practice file. Fill out the
code necessary to attain the correct information. 

NOTE: There is no checker for this practice. This is meant to be interactive 
and open to experimentation. There will be explanations on how to check your 
work with Postman.
"""

# Imports
from flask import Flask
from utils import movies

# TODO: Make a flask instance
app = 


# TODO: Complete the following endpoint so that it returns 
# TODO:     {"books": ["Fahrenheit 451", "Moby Dick", "Hunger Games"]}, 200
@app.route("/books", methods=["POST"])
def books():


# TODO: Register the `movies` endpoint with no prefix. The blueprint has been
# TODO:     imported for you. 


# Run the application
if __name__ == "__main__":
    print("\n\nNOTE: To test your implementations and if all is good, open")
    print("Postman and try out `http://127.0.0.1/books` and `http://127.0.0.1/movies`.")
    print("Remeber that the former is a POST endpointt the former is a GET endpoint.")
    print("To change HTTP methods on Postman, simply click on the GET text with a")
    print("down carrot to it and select your desired HTTP method!\n\n")
    app.run(debug=True)
