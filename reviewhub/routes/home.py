from flask import Blueprint, render_template, redirect, url_for, session

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    # redirect to login if not authenticated or in guest mode
    if not session.get('user_id') and not session.get('guest_mode'):
        return redirect(url_for('auth.login'))
    return render_template("home/index.html")

