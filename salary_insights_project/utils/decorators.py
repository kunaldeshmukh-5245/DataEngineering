import functools
import datetime

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] Called function '{func.__name__}' with args={args}, kwargs={kwargs}\n"
        with open("function_calls.log", "a") as log_file:
            log_file.write(log_line)
        return func(*args, **kwargs)
    return wrapper
    