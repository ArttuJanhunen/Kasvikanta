from application import db
from sqlalchemy import text


class PlantUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id', ondelete='CASCADE'), nullable=False)
    date_watered = db.Column(db.String(50), nullable=True)

    def __init__(self, user_id, plant_id):
        self.user_id = user_id
        self.plant_id = plant_id
        self.date_watered = "Kasvia ei vielä ole kasteltu"

    @staticmethod
    def amount_of_plants_for_user():
        stmt = text (
            "SELECT account.id, COUNT (*) FROM account, plant_user"
            " WHERE account.id = plant_user.user_id"
            " GROUP BY account.id"
        )

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id": row[0], "amount": row[1]})
        
        return response