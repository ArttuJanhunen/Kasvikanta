from flask_wtf import FlaskForm
from wtforms import StringField, validators


class FamilyForm(FlaskForm):
    name = StringField("Heimon nimi:", [validators.Length(min=2)])
    latin_name = StringField("Latinankielinen nimi:", [
                             validators.Length(min=2)])

    class Meta:
        csrf = False
