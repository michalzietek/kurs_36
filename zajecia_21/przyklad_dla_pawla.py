def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "aaaa!!!"
    return wrapper


@uppercase_decorator
@exclamation_decorator
def greet():
    return "hello world"

print(greet())  # Output: HELLO WORLD!!!