# 1
def mage_counter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter


# 2
def spell_accumulator(initial_power):
    def accumulate(x):
        nonlocal initial_power
        initial_power += x
        return initial_power

    return accumulate


# 3
def enchantment_factory(enchantment_type):
    def enchant(name):
        return enchantment_type + " " + name

    return enchant


def memory_vault():
    mem = {}

    def store(key, value):
        mem[key] = value

    def recall(key):
        return mem.get(key, "Memory not found")

    return {store: recall}


# Tests
# 1
print("\nTesting mage counter..")
counter_a = mage_counter()
counter_b = mage_counter()
print(f"counter_a call 1: {counter_a()}")
print(f"counter_a call 2: {counter_a()}")
print(f"counter_b call 1: {counter_b()}")

# 2
print("\nTesting spell accumulator..")
accumulator = spell_accumulator(100)
print(f"Base 100, add 20: {accumulator(20)}")
print(f"Base 100, add 30: {accumulator(30)}")

# 3

print("\nTesting enchantment factory...")
flaming_factory = enchantment_factory("Flaming")
frozen_factory = enchantment_factory("Frozen")
fl_sword = flaming_factory("sword")
fr_sword = frozen_factory("sword")
print(fl_sword)
print(fr_sword)

# 4
vault = memory_vault()
for k, v in vault.items():
    print("Store 'secret' = 42")
    k("secret", 42)
    print(f"Recall 'secret':  {v('secret')}")
    print(f"Recall 'unknown':  {v('unknown')}")
