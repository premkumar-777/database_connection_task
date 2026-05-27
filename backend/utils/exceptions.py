from fastapi import HTTPException
from utils.status_codes import BAD_REQUEST, NOT_FOUND


def user_not_found():
    return HTTPException(
        status_code=NOT_FOUND,
        detail="user not found"
    )


def bad_request():
    return HTTPException(
        status_code=BAD_REQUEST,
        detail="Bad request"
    )
