from flask import Blueprint, render_template, redirect, url_for, session
from db.database import get_all_movies

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    # A página home pode ser acessada sem login e com guest mode ativado
    # Porém a details não pode ser acessada sem login e com guest mode ativado
    movies = get_all_movies()
    return render_template("home/index.html", movies=movies)

