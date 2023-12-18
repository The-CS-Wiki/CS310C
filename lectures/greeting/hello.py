from flask import Blueprint

english = Blueprint("english", __name__)
french = Blueprint("french", __name__)
tagalog = Blueprint("tagalog", __name__)
madarin = Blueprint("madarin", __name__)


@english.route("/english", methods=["GET"])
def english_endpoint():
    return {"message": "HELLO !!!"}, 200


@french.route("/french", methods=["GET"])
def french_endpoint():
    return {"message": "SALUT !!!"}, 200


@tagalog.route("/tagalog", methods=["GET"])
def tagalog_endpoing():
    return {"message": "KUMUSTA !!!"}, 200


@madarin.route("/madarin", methods=["GET"])
def madarin_endpoint():
    return {"message": "NIHAO !!!"}, 200
