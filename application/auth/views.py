from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error="Käyttäjätunnus tai salasana väärin")

    print("Käyttäjä "+user.name+" tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/users/new", methods=["GET"])
def new_user():
    return render_template("/auth/new.html", form=NewUserForm())


@app.route("/users/new", methods=["POST"])
def user_create():
    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("/auth/new.html", form=form)

    newUser = User(form.name.data, form.username.data,
                   form.password.data, False)
    db.session().add(newUser)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/users/", methods=["GET"])
def users_index():

    if current_user.is_admin:
        return render_template("/auth/list.html", users=User.query.all())
    else:
        return redirect(url_for("index"))


@app.route("/users/delete/<user_id>", methods=["POST"])
def users_delete(user_id):
    certainUser = User.query.get(user_id)

    if current_user.is_admin:
        db.session().delete(certainUser)
        db.session().commit()

    return redirect(url_for("users_index"))
