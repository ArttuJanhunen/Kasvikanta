from application import app, db
from flask import render_template, request, redirect, url_for
from application.plants.models import Plant
from application.plants.forms import PlantForm, PlantCareInstructionsForm


@app.route("/plants", methods=["GET"])
def plants_index():
    return render_template("plants/list.html", plants=Plant.query.all())


@app.route("/plants/new/")
def plants_form():
    return render_template("/plants/new.html", form=PlantForm())


@app.route("/plants/", methods=["POST"])
def plants_create():
    form = PlantForm(request.form)

    if not form.validate():
        return render_template("/plants/new.html", form=form)

    newPlant = Plant(form.name.data, form.latin_name.data)
    db.session().add(newPlant)
    db.session().commit()

    return redirect(url_for("plants_index"))


@app.route("/plants/<plant_id>", methods=["GET"])
def plants_specific(plant_id):
    certainPlant = Plant.query.get(plant_id)
    print(certainPlant)

    return render_template("/plants/certainplant.html", plant=certainPlant, form=PlantCareInstructionsForm())


@app.route("/plants/update/<plant_id>", methods=["POST"])
def plants_update_care_instructions(plant_id):
    certainPlant = Plant.query.get(plant_id)

    form = PlantCareInstructionsForm(request.form)

    if not form.validate():
        return render_template("/plants/certainplant.html", plant=certainPlant, form=form)

    certainPlant.care_instructions = form.care_instructions.data
    db.session().commit()

    return redirect("/plants/"+str(certainPlant.id))
