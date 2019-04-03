from application import app, db
from flask import render_template, request, redirect, url_for
from application.family.models import Family
from application.family.forms import FamilyForm
from flask_login import login_required, current_user


@app.route("/families", methods=["GET"])
def families_index():
    return render_template("families/list.html", families=Family.query.all())


@app.route("/families/new/")
@login_required
def families_form():
    return render_template("/families/new.html", form=FamilyForm())


@app.route("/families/", methods=["POST"])
@login_required
def families_create():
    form = FamilyForm(request.form)
    print(form.name.data)
    print(form.latin_name.data)

    if not form.validate():
        return render_template("/families/new.html", form=form)

    newFamily = Family(form.name.data, form.latin_name.data)

    db.session().add(newFamily)
    db.session().commit()

    return redirect(url_for("families_index"))


@app.route("/families/delete/<family_id>", methods=["POST"])
@login_required
def family_delete(family_id):
    certainFamily = Family.query.get(family_id)

    if (current_user.is_admin):
        db.session().delete(certainFamily)
        db.session().commit()

    return redirect(url_for("families_index"))
