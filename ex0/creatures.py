from abc import ABC, abstractmethod


class Creature(ABC):
    """ """

    def __init__(self, name: str, type: str) -> None:
        """ """
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        """ """
        pass

    def describe(self) -> str:
        """ """
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """ """
        attack: str = "Ember"
        return f"{self.name} uses {attack}!"


class Pyrodon(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """ """
        attack: str = "Flamethrower"
        return f"{self.name} uses {attack}!"


class Aquabub(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """ """
        attack: str = "Water Gun"
        return f"{self.name} uses {attack}!"


class Torragon(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """ """
        attack: str = "Hydro Pump"
        return f"{self.name} uses {attack}!"


class CreatureFactory(ABC):
    """ """

    @abstractmethod
    def create_base(self) -> Creature:
        """ """
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """ """
        pass


class FlameFactory(CreatureFactory):
    """ """

    def create_base(self) -> Creature:
        """ """
        creature = Flameling()
        return creature

    def create_evolved(self) -> Creature:
        """ """
        creature = Pyrodon()
        return creature


class AquaFactory(CreatureFactory):
    """ """

    def create_base(self) -> Creature:
        """ """
        creature = Aquabub()
        return creature

    def create_evolved(self) -> Creature:
        """ """
        creature = Torragon()
        return creature


if __name__ == "__main__":
    flameling = Flameling()
    print(flameling.type)
    cf = AquaFactory()
    aquabub = cf.create_base()
    print(aquabub.name, aquabub.type)
    print(aquabub.describe())
