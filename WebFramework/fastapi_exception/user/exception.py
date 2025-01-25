from exception import BaseAPIException

class UserDoesNotExistsException(BaseAPIException):
    status_code = 10000
    detail = 'user does not exists'