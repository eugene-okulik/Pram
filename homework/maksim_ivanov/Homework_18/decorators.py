from functools import wraps


def log_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Выполнена функция: {func.__name__}")
        return result

    return wrapper
