from flask import request, render_template,Blueprint, redirect, url_for, flash 
from app.models import User 
from app.forms.authforms import RegisterForm, LoginForm 
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


bp=Blueprint("auth", __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))

    form=RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        hash=generate_password_hash(form.password.data)
        user.password_hash=hash 
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated :
        return redirect(url_for("skill.dashboard"))
    
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for("skill.dashboard"))
        flash("Invalid Credentials!")

    return render_template("login.html", form=form)

@bp.route("/logout")
@login_required 
def logout():
    logout_user()
    return redirect(url_for("auth.login"))