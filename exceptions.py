class BaseAppException(Exception):
    __slots__ = ["message", "code"]

    def __init__(self, message, code):
        self.message = message
        self.code = code


class AppException(BaseAppException):
    def __init__(self, message, code):
        super.__init__(message, code)
