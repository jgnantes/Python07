from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    """ """

    @abstractmethod
    def heal(self) -> str:
        """ """
        pass


class TransformCapability(ABC):
    """ """

    def __init__(self) -> None:
        """ """
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """ """
        pass

    @abstractmethod
    def revert(self) -> str:
        """ """
        pass


class Sproutling(Creature, HealCapability):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """ """
        move: str = "Vine Whip"
        return f"{self.name} uses {move}!"

    def heal(self) -> str:
        """ """
        return f"{self.name} heals itself for a small amount!"


class Bloomelle(Creature, HealCapability):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """ """
        move: str = "Petal Dance"
        return f"{self.name} uses {move}!"

    def heal(self) -> str:
        """ """
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    """ """

    def create_base(self) -> Creature:
        """ """
        return Sproutling()

    def create_evolved(self) -> Creature:
        """ """
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    """ """

    def __init__(self) -> None:
        """ """
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """ """
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        """ """
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """ """

    def __init__(self) -> None:
        """ """
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """ """
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        """ """
        self.transformed = True
        return f"{self.name} morphs into a dragonic form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    """ """

    def create_base(self) -> Creature:
        """ """
        return Shiftling()

    def create_evolved(self) -> Creature:
        """ """
        return Morphagon()
