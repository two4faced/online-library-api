from fastapi import HTTPException


class OnLibraryException(Exception):
    detail = 'unknown error'

    def __init__(self, *args):
        super().__init__(self.detail, *args)


class ObjectNotFound(OnLibraryException):
    detail = 'object was not found'


class InvalidCredentialsException(OnLibraryException):
    detail = 'invalid password or username'


class OnLibraryHTTPException(HTTPException):
    status_code = 500
    detail = 'unknown error'

    def __init__(self):
        super().__init__(self.status_code, self.detail)


class InvalidCredentialsHTTPException(OnLibraryHTTPException):
    status_code = 401
    detail = 'invalid password or username'
