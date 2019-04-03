from application import app, db
from flask import render_template, request, redirect, url_for
from application.plants.models import Plant
from application.plants.forms import PlantForm, PlantCareInstructionsForm, PlantImageForm
from application.family.models import Family
from flask_login import login_required, current_user


@app.route("/plants", methods=["GET"])
def plants_index():
    return render_template("plants/list.html", plants=Plant.query.all(), families=Family.find_families_with_plants())


@app.route("/plants/new/")
@login_required
def plants_form():
    form = PlantForm()
    families = Family.query.all()
    family_list = [(family.id, family.name) for family in families]
    form.family_id.choices = family_list

    return render_template("/plants/new.html", form=form)


@app.route("/plants/", methods=["POST"])
@login_required
def plants_create():
    form = PlantForm(request.form)
    families = Family.query.all()
    family_list = [(family.id, family.name) for family in families]
    form.family_id.choices = family_list
    if not form.validate():
        return render_template("/plants/new.html", form=form)

    newPlant = Plant(form.name.data, form.latin_name.data, form.family_id.data)
    db.session().add(newPlant)
    db.session().commit()

    return redirect(url_for("plants_index"))


@app.route("/plants/<plant_id>", methods=["GET"])
def plants_specific(plant_id):
    certainPlant = Plant.query.get(plant_id)

    return render_template("/plants/certainplant.html", plant=certainPlant, form=PlantCareInstructionsForm())


@app.route("/plants/update/<plant_id>", methods=["POST"])
@login_required
def plants_update_care_instructions(plant_id):
    certainPlant = Plant.query.get(plant_id)

    form = PlantCareInstructionsForm(request.form)

    if not form.validate():
        return render_template("/plants/certainplant.html", plant=certainPlant, form=form)

    certainPlant.care_instructions = form.care_instructions.data
    db.session().commit()

    return redirect("/plants/"+str(certainPlant.id))


@app.route("/plants/updateimg/<plant_id>", methods=["POST"])
@login_required
def plants_update_plant_image(plant_id):
    certainPlant = Plant.query.get(plant_id)

    certainPlant.plant_image = request.form.get("plant_image")
    db.session().commit()

    return redirect("/plants/"+str(certainPlant.id))


@app.route("/plants/delete/<plant_id>", methods=["POST"])
@login_required
def plant_delete(plant_id):
    certainPlant = Plant.query.get(plant_id)

    if current_user.is_admin:
        db.session().delete(certainPlant)
        db.session().commit()

    return redirect(url_for("plants_index"))
