from app import db


class Imports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    def toJSON(self):
        return {
            'import_id': self.id
        }