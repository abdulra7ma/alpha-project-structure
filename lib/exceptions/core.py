# external imports
from rest_framework.exceptions import APIException


class ObjectNotFound(APIException):
    """Raise a HTTP 404 error when the Object not found in the DB"""

    status_code = 404
    default_detail = "Object Not Found"
    default_code = "object_not_found"


class ObjectQueryIdNotFound(APIException):
    """Raise a HTTP 404 error when the Object id not the query params"""

    status_code = 404
    default_detail = "object id not specified in the query params"
    default_code = "object_query_id_not_found"


class NotIntegerType(APIException):
    """Raise a HTTP 404 error when the Object id not an integer type"""

    status_code = 404
    default_detail = "object id must be in an integer form"
    default_code = "not_integer_id"


class InvaildToken(APIException):
    """Raise a HTTP 400 error when the Token is invalid"""

    status_code = 400
    default_code = "invalid_token"

    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
