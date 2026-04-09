import ex1
from typing import cast


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("  base:")
    hcf = ex1.HealingCreatureFactory()
    sproutling = cast(ex1.capabilities.Sproutling, hcf.create_base())
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print("  evolved:")
    bloomelle = cast(ex1.capabilities.Bloomelle, hcf.create_evolved())
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")
    print("  base:")
    tcf = ex1.TransformCreatureFactory()
    shiftling = cast(ex1.capabilities.Shiftling, tcf.create_base())
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print("  evolved:")
    morphagon = cast(ex1.capabilities.Morphagon, tcf.create_evolved())
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())
