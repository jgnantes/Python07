from ex0 import CreatureFactory, FlameFactory, AquaFactory


def verify(factory: CreatureFactory) -> None:
    """ """
    print("Testing factory")
    try:
        base_creature = factory.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        evolved_creature = factory.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())
    except AttributeError as e:
        print(f"Error: {e}")
        print(f"{factory} could not make creatures")
        return None


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    """ """
    print("Testing battle")
    try:
        base_1 = factory_1.create_base()
        print(base_1.describe())
        print("  vs.")
        base_2 = factory_2.create_base()
        print(base_2.describe())
        print("  fight!")
        print(base_1.attack())
        print(base_2.attack())
    except AttributeError as e:
        print(f"Error: {e}")
        print("The factores could not make battling creatures")


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    verify(ff)
    print("")
    verify(af)
    print("")
    battle(ff, af)
