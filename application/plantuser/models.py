from application import db


class PlantUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey('Account.id', ondelete='CASCADE'), nullable=False)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, user_id, plant_id):
        self.user_id = user_id
        self.plant_id = plant_id
