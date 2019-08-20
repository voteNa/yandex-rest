from sqlalchemy import Integer
from sqlalchemy.dialects import postgresql

from app import db


class Citizen(db.Model):
    citizen_id = db.Column(db.Integer, primary_key=True)
    import_id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.Text)
    street = db.Column(db.Text)
    building = db.Column(db.Text)
    apartment = db.Column(db.Integer)
    name = db.Column(db.Text)
    birth_date = db.Column(db.DateTime)
    gender = db.Column(db.Text)
    relatives = db.Column(postgresql.ARRAY(Integer))

    def toJSON(self):
        return {
            'citizen_id': self.citizen_id,
            'town': self.town,
            'street': self.street,
            'building': self.building,
            'apartment': self.apartment,
            'name': self.name,
            'birth_date': self.birth_date.strftime("%d.%m.%Y"),
            'gender': self.gender,
            'relatives': self.relatives,
        }
