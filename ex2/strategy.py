from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.capabilities import HealCapability as hc, TransformCapability as tc


class BattleStrategy(ABC):
    """ """

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """ """
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """ """
        pass


class NormalStrategy(BattleStrategy):
    """ """

    def is_valid(self, creature: Creature) -> bool:
        """ """
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> str:
        """ """
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """ """

    def is_valid(self, creature: Creature) -> bool:
        """ """
        if isinstance(creature, Creature) and isinstance(creature, tc):
            return True
        return False

    def act(self, creature: Creature) -> str:
        """ """
        string: str = ""
        if self.is_valid(creature):
            creature_tc: tc = cast(tc, creature)
            string = creature_tc.transform() + "\n"
            string += creature.attack() + "\n"
            string += creature_tc.revert()
            return string
        else:
            string = "Battle error, aborting tournament: Invalid Creature "
            string += f"{creature.name} for this aggressive strategy"
            raise Exception(string)


class DefensiveStrategy(BattleStrategy):
    """ """

    def is_valid(self, creature: Creature) -> bool:
        """ """
        if isinstance(creature, Creature) and isinstance(creature, hc):
            return True
        return False

    def act(self, creature: Creature) -> str:
        """ """
        string: str = ""
        if self.is_valid(creature):
            creature_hc: hc = cast(hc, creature)
            string += creature.attack() + "\n"
            string += creature_hc.heal()
            return string
        else:
            string = "Battle error, aborting tournament: Invalid Creature "
            string += f"{creature.name} for this defensive strategy"
            raise Exception(string)
