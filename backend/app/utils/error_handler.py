from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def handle_db_exceptions(func):
    """
    Decorator to handle database exceptions and rollback transactions in case of an error.

    :param func: Function to be decorated
    :return: Wrapped function with error handling
    """

    def wrapper(*args, **kwargs):
        db = kwargs.get("db", None)
        if db is None:
            raise ValueError("Database session must be provided as 'db' argument")

        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            if db:
                db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return wrapper
