import functools
import operator
from typing import Callable, Any
from functools import lru_cache
from functools import singledispatch


# 1
def spell_reducer(spells, operation):
    try:
        if len(spells) == 0:
            return 0
        return functools.reduce(operation, spells)
    except Exception as e:
        print(e)


# 2

base_func = lambda power, element, target: f"{element} {power} {target}"


def partial_enchanter(base_enchantment: Callable):
    a = functools.partial(base_enchantment, 50, "a")
    b = functools.partial(base_enchantment, 50, "b")
    c = functools.partial(base_enchantment, 50, "c")
    return {a("aga"): a, b("aga"): b, c("aga"): c}


# 3

@lru_cache()
def memoized_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# 4


def spell_dispatcher():
    @singledispatch
    def cast(spell: Any):
        print("Unknown spell type")

    @cast.register(int)
    def damage_spell(spell: int):
        print(f"Damage spell: {spell} damage")

    @cast.register(str)
    def enchantment(spell: str):
        print(f"Enchantment: {spell}")

    @cast.register(list)
    def multi_cast(spell: list):
        print(f"Multi-cast: {len(spell)} spells")

    return cast


# Tests

# 1
print("\nTesting spell reducer...")
print("Sum: ", spell_reducer([6, 7], operator.add))
print("Product: ", spell_reducer([6, 7], operator.mul))
print("Max: ", spell_reducer([6, 7], max))

# 2
print("\nTesting partial enchanter...")
d = partial_enchanter(base_func)
for k in d.keys():
    print(k)

# 3
print("\nTesting memoized fibonacci...")
print(f"Fib(0): {memoized_fibonacci(0)}")
print(f"Fib(1): {memoized_fibonacci(1)}")
print(f"Fib(10): {memoized_fibonacci(10)}")
print(f"Fib(15): {memoized_fibonacci(15)}")
# print(memoized_fibonacci.cache_info())

# 4
print("\nTesting spell dispatcher...")

disp = spell_dispatcher()

disp(10)
disp(2.2)
disp([1, 2, 3])
disp("alo")
