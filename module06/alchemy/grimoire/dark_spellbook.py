from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    if 'VALID' in validation:
        return f"Spell recorded: {spell_name} {validation}"
    else:
        return f"Spell rejected: {spell_name} {validation}"
