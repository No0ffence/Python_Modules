import datetime
import string
from functools import wraps
from typing import Callable


# 1
# todo time
def spell_timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        delta = datetime.datetime.now() - start_time
        print(
            f"Spell completed in {delta.total_seconds()} seconds")
        return result

    return wrapper


# 2
def power_validator(min_power):
    def power_validator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs["power"]
            if power >= min_power:
                res = func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
            return res

        return wrapper

    return power_validator


# 3
def retry_spell(max_attempts):
    def retry_spell(func):
        def wrapper(*argc, **kwargs):
            i = 0
            while i < max_attempts:
                try:
                    i += 1
                    res = func(*argc, **kwargs)

                    return res
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return retry_spell


# 4
class MageGuild:
    @staticmethod
    def validate_mage_name(name):
        for c in name:
            if c not in string.ascii_letters and c not in " ":
                return False
        return len(name) >= 3

    @power_validator(10)
    def cast_spell(self, spell_name, power):
        return f"Successfully cast {spell_name} with {power} power"


# Tests

# 1
@spell_timer
def cast(spell):
    return f"Casting {spell}"


print("Testing spell timer...")
print(f"Result: {cast('Fireball')}")


# 2
@power_validator(101)
def test_power(spell, power):
    return f"Casting {spell}"


print("Testing spell power...")
print(f"Result: {test_power(spell='Fireball', power=1000)}")


# 3

@retry_spell(3)
def failed_func(spell):
    1 + "x"
    return f"Casting {spell}"


@retry_spell(3)
def good_func():
    return "Waaaaaaagh spelled !"


print("Testing retrying spell...")
print(f"{failed_func('Fireball')}")
print(f"{good_func()}")

# 4

g_name = "Ebalay"
b_name = "ebalay12"
print(MageGuild.validate_mage_name(g_name))
print(MageGuild.validate_mage_name(b_name))

guild = MageGuild()
print(guild.cast_spell("Lightning", power=15))
print(guild.cast_spell("Lightning", power=9))
