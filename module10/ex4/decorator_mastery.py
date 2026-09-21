import datetime
from functools import wraps
from typing import Callable


def spell_timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        time = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(
            f"Spell completed in {datetime.datetime.now() - time} seconds")
        return result

    return wrapper


@spell_timer
def cast(spell):
    return f"Casting {spell}"


print("Testing spell timer...")
print(f"Result {cast('Fireball')}")
