from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "PATCH"])
#la fonction ouvre le fichier JSON afin de récupérer ce qu'il se trouve
def acceuil():
    if request.method == "GET":
        with open('user.JSON') as mon_fichier:
            data = json.load(mon_fichier)
        return make_response( "ok",200)

    elif request.method == "POST":
        id = request.args["id"]
        with open(id+'.txt', 'w') as mon_fichier:
            json.dump(request.get_json(), mon_fichier)
        return make_response("ok", 200)


if (__name__) == '__main__':
    app.run(
        host="0.0.0.0",
        port=8081,
        debug=True,
    )