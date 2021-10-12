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

        print(data)

        pass
    #elif request.method == "POST":
    user2 = {
        "prenom": "Michel",
        "nom": "DUBOIS",
    }

    with open('user.JSON', 'w') as mon_fichier:
        json.dump(user2, mon_fichier)
    pass

    print(f"arguments : {request.args}")
    print(f"body: {request.get_json()}")


    return make_response(user2, 200)


if (__name__) == '__main__':
    app.run(
        host="0.0.0.0",
        port=8081,
        debug=True,
    )
