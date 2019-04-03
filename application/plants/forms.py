from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField


class PlantForm(FlaskForm):
    name = StringField("Kasvin nimi:", [validators.Length(min=2)])
    latin_name = StringField("Latinankielinen nimi:", [
                             validators.Length(min=2)])
    family_id = SelectField("Kasvin heimo:", coerce=int)

    class Meta:
        csrf = False


class PlantCareInstructionsForm(FlaskForm):
    care_instructions = StringField("", [validators.Length(min=2)])

    class Meta:
        csrf = False


class PlantImageForm(FlaskForm):
    plant_image = StringField("", [validators.Length(min=2)])

    class Meta:
        csrf: False
