from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus:")
    password = PasswordField("Salasana:")

    class Meta:
        csrf = False


class NewUserForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(
        min=3), validators.Length(max=150)])
    username = StringField("Käyttäjätunnus:", [
                           validators.Length(min=3), validators.Length(max=150)])
    password = PasswordField(
        "Salasana:", [validators.Length(min=3), validators.Length(max=150)])

    class Meta:
        csrf = False
