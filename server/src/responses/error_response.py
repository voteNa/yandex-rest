from src.responses.base_response import BaseResponse


class ErrorResponse(BaseResponse):

    def toJSON(self,):
        return {'Error': self.data}, self.httpStatus
