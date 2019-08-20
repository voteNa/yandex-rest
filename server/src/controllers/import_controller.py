from datetime import datetime


def import_post(body=None):
    from app import db
    from src.entities.citizen import Citizen
    from src.entities.imports import Imports
    from src.repository.ImportRepo import ImportRepo
    from src.responses.error_response import ErrorResponse

    # Validate
    citizen_ids = set()
    relatives_ids = set()
    relative_map = {}
    for el in body['citizens']:
        if el['citizen_id'] in citizen_ids:
            return ErrorResponse('Not Unique citizen_id', 400).toJSON()

        citizen_ids.add(el['citizen_id'])
        relatives_ids = relatives_ids.union(set(el.get('relatives')))
        relative_map[el['citizen_id']] = el.get('relatives')

        try:
            birthday = datetime.strptime(el['birth_date'], '%d.%m.%Y')
            if birthday > datetime.now():
                raise ValueError
        except ValueError:
            return {'error': 'bad Date'}, 400
    if relatives_ids.difference(citizen_ids):
        return ErrorResponse('bad Relatives ID', 400).toJSON()

    for citizen_id in relative_map:
        relative = relative_map.get(citizen_id)
        if not relative:
            continue

        for relative_id in relative:
            if citizen_id not in relative_map.get(relative_id):
                return ErrorResponse('bad Relatives connexion', 400).toJSON()
    # Save

    imports = Imports(data=body['citizens'])
    ImportRepo().save(imports)
    from src.responses.object_response import ObjectResponse
    return ObjectResponse(imports, 201).toJSON()