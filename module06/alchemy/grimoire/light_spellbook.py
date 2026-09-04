from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    if 'VALID' in validation:
        return f"Spell recorded: {spell_name} {validation}"
    else:
        return f"Spell rejected: {spell_name} {validation}"
