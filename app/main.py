from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in result:
            calculation = func(*args, **kwargs)
            result[key] = calculation
            print("Calculating new result")
            return calculation
        else:
            print("Getting from cache")
            return result[key]
    return wrapper
