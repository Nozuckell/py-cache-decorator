from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args not in result:
            calculation = func(*args, **kwargs)
            result[args] = calculation
            print("Calculating new result")
            return calculation
        else:
            print("Getting from cache")
            return result[args]
    return wrapper
