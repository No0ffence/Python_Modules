from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for a in allowed:
        if a in ingredients:
            return f"({ingredients}- VALID)"
    return f"({ingredients}- INVALID)"
