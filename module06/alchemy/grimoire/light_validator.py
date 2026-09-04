def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    for a in allowed:
        if a in ingredients:
            return f"({ingredients}- VALID)"
    return f"({ingredients}- INVALID)"
