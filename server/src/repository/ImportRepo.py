from datetime import datetime

from src.entities.imports import Imports


class ImportRepo:
    def getImport(self, import_id: int):
        return Imports.query.filter(Imports.id == import_id).first()

    def save(self, imports: Imports):
        from src.entities import Citizen
        from app import db

        db.session.add(imports)
        db.session.commit()

        for el in imports.data:
            el['import_id'] = imports.id
            date = datetime.strptime(el['birth_date'], '%d.%m.%Y')
            el['birth_date'] = date.strftime('%m.%d.%Y')
            importItem = Citizen(**el)
            db.session.add(importItem)
        db.session.commit()
