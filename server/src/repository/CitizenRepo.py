from app import db
from src.entities.citizen import Citizen


class CitizenRepo:
    def getCitizen(self, citizen_id: int, import_id: int):
        return Citizen.query.filter(Citizen.import_id == import_id, Citizen.citizen_id == citizen_id).first()

    def getCitizenList(self, import_id: int):
        return Citizen.query.filter(Citizen.import_id == import_id).all()

    def saveWithRelation(self, citizen: Citizen, forDelete: set, forAdded: set):
        db.session.add(citizen)
        if forAdded:
            db.session.execute('''
            with add as (
                select citizen_id, relatives from citizen
                where citizen_id in (%s) and import_id = :import_id
            )
            update citizen c
            set relatives = array_append(add.relatives, :citizen_id)
            from add
            where c.citizen_id = add.citizen_id and import_id = :import_id
            ''' % str(forAdded)[1:-1], {'citizen_id': citizen.citizen_id, 'import_id': citizen.import_id})
        if forDelete:
            db.session.execute('''
            with del as (
                select citizen_id, relatives from citizen
                where citizen_id in (%s) and import_id = :import_id
            )
            update citizen c
            set relatives = array_remove(del.relatives, :citizen_id)
            from del
            where c.citizen_id = del.citizen_id and import_id = :import_id
            ''' % str(forDelete)[1:-1], {'citizen_id': citizen.citizen_id, 'import_id': citizen.import_id})
        db.session.commit()

    def save(self, citizen: Citizen):
        db.session.add(citizen)
        db.session.commit()

