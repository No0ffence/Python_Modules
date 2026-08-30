from module06.elements import *
from alchemy.elements import *


def healing_potion():
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion():
    return (f"Strength potion brewed "
            f"with '{create_fire()}' and '{create_water()}'")


def agility_potion():
    return (f"Agility potion brewed "
            f"with '{create_air()}' and '{create_water()}'")
