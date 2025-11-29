from flask import Blueprint, render_template, session, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")


@auth_bp.route("/register")
def register():
    return render_template("auth/register.html")


@auth_bp.route("/guest")
def guest_login():
    session['guest_mode'] = True
    return redirect(url_for("home.homepage"))


@auth_bp.route("/logout")
def logout():
    # clear user session and redirect to login
    session.pop("user_id", None)
    session.pop("guest_mode", None)
    return redirect(url_for("auth.login"))
