"decorators"
import sys
from functools import wraps

from app.err import err_obj


def try_catch(func):
    """
    Generic decorator that will return an error object on exception.
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            exc_tb = sys.exc_info()[2]
            top_frame = exc_tb
            while top_frame.tb_next:
                top_frame = top_frame.tb_next
            filename = top_frame.tb_frame.f_code.co_filename
            lineno = top_frame.tb_lineno
            return err_obj(func.__name__, f"{filename}:{lineno}", error), 500

    return decorated
