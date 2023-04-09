from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from src.leaderboard import Leaderboard
from src.models import Score


app = Flask(__name__)
Bootstrap(app)

leaderboard = Leaderboard()

@app.route("/")
def index():
    scores = leaderboard.get_scores()
    return render_template("index.html",
                            scores=scores)

@app.route("/player", methods=["GET", "POST"])
def player():
    avatars = leaderboard.get_avatar_dic()

    return render_template("player.html", score = score, avatars = avatars)
