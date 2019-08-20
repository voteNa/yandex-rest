from src.responses.error_response import ErrorResponse
from src.responses.object_response import ObjectResponse


def birthday_stat(import_id=None):
    from src.repository.ImportRepo import ImportRepo
    from src.repository.stats_repo import StatsRepo

    importObj = ImportRepo().getImport(import_id=import_id)
    if importObj is None:
        return ErrorResponse("Not Found", 404).toJSON()

    result = StatsRepo().getBirthday(import_id=import_id)
    return ObjectResponse(data=result, httpStatus=200).toJSON()


def percentile_stat(import_id=None):
    from src.repository.ImportRepo import ImportRepo
    from src.repository.stats_repo import StatsRepo

    importObj = ImportRepo().getImport(import_id=import_id)
    if importObj is None:
        return ErrorResponse("Not Found", 404).toJSON()

    result = StatsRepo().getPercentile(import_id=import_id)
    return ObjectResponse(data=result, httpStatus=200).toJSON()
