from flask import Flask
from greeting.hello import english, french, tagalog, madarin

app = Flask(__name__)

app.register_blueprint(english, url_prefix="/greeting")
app.register_blueprint(french, url_prefix="/greeting")
app.register_blueprint(tagalog, url_prefix="/greeting")
app.register_blueprint(madarin, url_prefix="/greeting")

app.route("/greeting/hello", methods=["GET"])


def hello():
    return {"message": "hello!"}, 200


if __name__ == "__main__":
    app.run(debug=True)