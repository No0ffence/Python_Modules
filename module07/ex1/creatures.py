from .capabilities import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses  Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return f"{self._name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self, target: str = "itself") -> str:
        return f"{self._name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._transform = 0

    def attack(self) -> str:
        return f"{self._name} attacks normally." if self._transform == 0 else \
            f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._transform = 1
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transform = 0
        return f"{self._name} returns to normal"


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transform = 0

    def attack(self) -> str:
        return f"{self._name} attacks normally." if self._transform == 0 else \
            f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._transform = 1
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transform = 0
        return f"{self._name} stabilizes its form"
