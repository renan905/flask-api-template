from flask import blueprints

main = blueprints.Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
    return "The Aplication is Online", 200