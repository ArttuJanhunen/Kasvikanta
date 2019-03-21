from application import app, db
from flask import render_template, request, redirect, url_for
from application.plants.models import Plant


@app.route("/plants", methods=["GET"])
def plants_index():
  return render_template("plants/list.html", plants=Plant.query.all())

@app.route("/plants/new/")
def plants_form():
    return render_template("/plants/new.html")


@app.route("/plants/", methods=["POST"])
def plants_create():
    print(request.form.get("name"))
    print(request.form.get("latin_name"))

    newPlant = Plant(request.form.get("name"), request.form.get("latin_name"))
    db.session().add(newPlant)
    db.session().commit()

    return redirect(url_for("plants_index"))

@app.route("/plants/<plant_id>", methods=["GET"])
def plants_specific(plant_id):
  certainPlant= Plant.query.get(plant_id)
  print(certainPlant)

  return render_template("/plants/certainplant.html", plant=certainPlant)

@app.route("/plants/update/<plant_id>", methods=["POST"])
def plants_update_care_instructions(plant_id):
  certainPlant= Plant.query.get(plant_id)
  certainPlant.care_instructions = request.form.get("care_instructions")
  print('care instructions:')
  print(request.form.get("care_instructions"))

  db.session().commit()

  return redirect("/plants/"+str(certainPlant.id))

