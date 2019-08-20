from src.responses.base_response import BaseResponse


class ObjectResponse(BaseResponse):

    def toJSON(self, ):
        responseData = {
            'data': self.data.toJSON()
        }
        return responseData, self.httpStatus