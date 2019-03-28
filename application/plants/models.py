from application import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(150), nullable=False)
    latin_name = db.Column(db.String(150), nullable=False)
    care_instructions = db.Column(db.String(300), nullable=False)
    plant_image = db.Column(db.String(300), nullable=False)


    def __init__(self, name, latin_name):
        self.name = name
        self.latin_name = latin_name
        self.care_instructions = ''
        self.plant_image = ''
