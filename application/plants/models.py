from application import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(150), nullable=False)
    latin_name = db.Column(db.String(150), nullable=False)
    care_instructions = db.Column(db.String(600), nullable=False)
    plant_image = db.Column(db.String(300), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey(
        'family.id', ondelete='CASCADE'), nullable=False)

    plantusers = db.relationship(
        "PlantUser", cascade="all,delete", backref='plant', lazy=True)

    def __init__(self, name, latin_name, family_id):
        self.name = name
        self.latin_name = latin_name
        self.care_instructions = ''
        self.plant_image = ''
        self.family_id = family_id
