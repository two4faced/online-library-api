from fastapi import HTTPException


class OnLibraryException(Exception):
    detail = 'unknown error'

    def __init__(self, *args):
        super().__init__(self.detail, *args)


class ObjectNotFound(OnLibraryException):
    detail = 'object was not found'


class InvalidCredentialsException(OnLibraryException):
    detail = 'invalid password or username'


class InvalidTokenException(OnLibraryException):
    detail = 'invalid token'


class OnLibraryHTTPException(HTTPException):
    status_code = 500
    detail = 'unknown error'

    def __init__(self):
        super().__init__(self.status_code, self.detail)


class InvalidCredentialsHTTPException(OnLibraryHTTPException):
    status_code = 401
    detail = 'invalid password or username'


class InvalidTokenHTTPException(OnLibraryHTTPException):
    status_code = 401
    detail = 'invalid token'


class NotAuthenticatedHTTPException(OnLibraryHTTPException):
    status_code = 401
    detail = 'you are not logged in'


class NotEnoughPermissionsHTTPException(OnLibraryHTTPException):
    status_code = 403
    detail = 'not enough permissions'
