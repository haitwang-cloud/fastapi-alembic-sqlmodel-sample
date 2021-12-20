from app.models.models import User
from app.db.init import Session
from sqlalchemy.exc import InvalidRequestError
from app.utils.log_init import logger_loguru as logger


def get_users():
    # Session option #1
    result = None
    try:
        result = Session().query(User).all()
    except InvalidRequestError as e:
        logger.error(e)
        Session().rollback()


    finally:
        Session.remove()
        return result


def add_user(user):
    # Session option # 2
    with Session() as session:
        user = User(email=user.email)
        session.add(user)
        session.commit()
        return user
