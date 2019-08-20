from src.responses.error_response import ErrorResponse
from src.responses.list_response import ListResponse
from src.responses.object_response import ObjectResponse


def citizen_patch(import_id=None, citizen_id=None, body=None):
    from src.form.citizenEditForm import CitizenEditForm
    from src.services.citizen_service import CitizenService
    from src.repository.CitizenRepo import CitizenRepo

    citizen = CitizenRepo().getCitizen(citizen_id=citizen_id, import_id=import_id)
    if citizen is None:
        return ErrorResponse("Not Found", 404).toJSON()

    form = CitizenEditForm(citizen=citizen, data=body)
    if form.validate():
        CitizenService().editCitizen(citizen=citizen, form=form)
    else:
        return ErrorResponse(data='bad data', httpStatus=400).toJSON()

    return ObjectResponse(data=citizen, httpStatus=200).toJSON()


def citizen_list(import_id=None):
    from src.repository.CitizenRepo import CitizenRepo
    citizenList = CitizenRepo().getCitizenList(import_id=import_id)
    if not citizenList:
        return ErrorResponse("Not Found", 404).toJSON()

    return ListResponse(data=citizenList, httpStatus=200).toJSON()
