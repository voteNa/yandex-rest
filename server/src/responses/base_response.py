from abc import ABC, abstractmethod


class BaseResponse(ABC):
    httpStatus = int
    data = any

    def __init__(self, data, httpStatus: int):
        self.httpStatus = httpStatus
        self.data = data

    @abstractmethod
    def toJSON(self, ):
        pass