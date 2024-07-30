# decorators/log_decorator.py

import functools
import logging
import datetime


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_format = f"{datetime.datetime.now()} - {func.__name__} - "
            try:
                result = func(*args, **kwargs)
                log_message = f"{log_format}ok"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{log_format}error: {type(e).__name__}. Inputs: {args}, {kwargs}, {e}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                raise

        return wrapper

    if callable(filename):
        func = filename
        filename = None
        return decorator(func)

    return decorator
