from application import db
from sqlalchemy.sql import text


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(150), nullable=False)
    latin_name = db.Column(db.String(150), nullable=False)

    plants = db.relationship("Plant", backref='family', lazy=True)

    def __init__(self, name, latin_name):
        self.name = name
        self.latin_name = latin_name

    @staticmethod
    def find_families_with_plants():
        stmt = text("SELECT Family.id, Family.name FROM Family"
                    " LEFT JOIN Plant ON Plant.family_id = Family.id"
                    " GROUP BY Family.id"
                    " HAVING COUNT(Plant.id)>0")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response
