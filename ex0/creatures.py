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
        move: str = "Ember"
        return f"{self.name} uses {move}!"


class Pyrodon(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """ """
        move: str = "Flamethrower"
        return f"{self.name} uses {move}!"


class Aquabub(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """ """
        move: str = "Water Gun"
        return f"{self.name} uses {move}!"


class Torragon(Creature):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """ """
        move: str = "Hydro Pump"
        return f"{self.name} uses {move}!"


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

    def create_base(self) -> Flameling:
        """ """
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        """ """
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """ """

    def create_base(self) -> Aquabub:
        """ """
        return Aquabub()

    def create_evolved(self) -> Torragon:
        """ """
        return Torragon()


if __name__ == "__main__":
    flameling = Flameling()
    print(flameling.type)
    cf = AquaFactory()
    aquabub = cf.create_base()
    print(aquabub.name, aquabub.type)
    print(aquabub.describe())
