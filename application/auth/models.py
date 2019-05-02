from application import db
from sqlalchemy import text


class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    plantusers = db.relationship(
        "PlantUser", cascade="all,delete", backref='account', lazy=True)

    def __init__(self, name, username, password, is_admin):
        self.name = name
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def user_is_admin(self):
        return self.is_admin
