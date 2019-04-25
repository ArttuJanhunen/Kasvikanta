from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, TextAreaField


class PlantForm(FlaskForm):
    name = StringField("Kasvin nimi:", [validators.Length(
        min=2), validators.Length(max=150)])
    latin_name = StringField("Latinankielinen nimi:", [
                             validators.Length(min=2), validators.Length(max=150)])
    family_id = SelectField("Kasvin heimo:", coerce=int)

    class Meta:
        csrf = False


class PlantCareInstructionsForm(FlaskForm):
    care_instructions = TextAreaField(
        "", [validators.Length(min=2), validators.Length(max=600)])

    class Meta:
        csrf = False


class PlantImageForm(FlaskForm):
    plant_image = StringField(
        "", [validators.Length(min=2), validators.Length(max=300)])

    class Meta:
        csrf: False
