from elements import create_fire, create_water
from alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed "
            f"with '{create_fire()}' and '{create_water()}'")


def agility_potion() -> str:
    return (f"Agility potion brewed "
            f"with '{create_air()}' and '{create_water()}'")
