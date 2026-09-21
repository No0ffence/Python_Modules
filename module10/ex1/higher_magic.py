# spells
heal = lambda target, power: f"Heal restores {target} for {power} HP"
fireball = lambda target, power: f"Fireball hits {target} for {power} HP"
condition = lambda target, power: True if power > 100 else False

# aga
# 1
spell_combiner = (
    lambda spell1, spell2: lambda target, power: (spell1(target, power),
                                                  spell2(target, power))
)
# 2
power_amplifier = (
    lambda base_spell, multiplier: lambda target, power:
    base_spell(target, power * multiplier)
)
# 3
conditional_caster = (
    lambda condition, spell: lambda target, power: spell(target,
                                                         power) if condition(
        target, power) else "Spell fizzled"
)
# 4
spell_sequence = (
    lambda spells: lambda target, power: list(
        map(lambda func: func(target, power),
            spells))
)

# test
# todo
# pretty output
test_values = [18, 23, 7]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

# 1
combined = spell_combiner(fireball, heal)

print(combined("Dragon", 20))
# 2
mega_fireball = power_amplifier(fireball, 3)

print(mega_fireball('Goblin', 7))
# 3
try_cast = conditional_caster(condition, fireball)

print(try_cast("Goblin", 101))
# 4
sequence = spell_sequence([fireball, heal])

print(sequence("Goblin", 20))
