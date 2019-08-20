from src.responses.base_response import BaseResponse


class ListResponse(BaseResponse):

    def toJSON(self, ):
        responseData = {
            'data': []
        }
        for item in self.data:
            responseData['data'].append(item.toJSON())

        return responseData, self.httpStatus