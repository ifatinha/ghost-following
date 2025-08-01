
from flask import Flask, render_template, request
from util.ghost_following import get_ghost_following, export_to_csv


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():

    usernames = []

    if request.method == "POST":
        username = request.form.get("username")

        if username:
            # lógica de busca
            usernames = list(get_ghost_following(username))
            # Salva para download ou logs
            export_to_csv(usernames)
            return render_template("index.html", usernames=usernames, searched=True)

    # Passa os dados para o HTML
    return render_template("index.html", usernames=usernames, searched=False)


if __name__ == "__main__":
    app.run(debug=True)
