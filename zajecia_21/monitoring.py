import time
from datetime import datetime


def monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_datetime = datetime.now()
        try:
            result = func(*args, **kwargs)
            status = "Success"
            return result
        except Exception as e:
            status = f"Error: {e}"
        finally:
            end_time = time.time()
            duration = end_time - start_time
            log_line = (f"{start_datetime} - Function {func.__name__}, executed in {duration:.4f} seconds, "
                        f"Arguments: {args}, {kwargs} Status: {status}")
            with open("monitoring.log", "a+") as log:
                log.write(log_line + "\n")
    return wrapper
