import ex0
import ex1
import ex2


if __name__ == "__main__":
    fcf = ex0.FlameFactory()
    acf = ex0.AquaFactory()
    hcf = ex1.HealingCreatureFactory()
    tcf = ex1.TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print("  [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("\n* Battle *")
    flameling = fcf.create_base()
    sproutling = hcf.create_base()
    print(flameling.describe())
    print("  vs.")
    print(sproutling.describe())
    print("  now fight!")
    print(ex2.NormalStrategy().act(flameling))
    print(ex2.DefensiveStrategy().act(sproutling))

    print("\nTournament 1 (error)")
    print("  [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("\n* Battle *")
    flameling = fcf.create_base()
    sproutling = hcf.create_base()
    print(flameling.describe())
    print("  vs.")
    print(sproutling.describe())
    print("  now fight!")
    try:
        print(ex2.AggressiveStrategy().act(flameling))
        print(ex2.DefensiveStrategy().act(sproutling))
    except Exception as e:
        print(e)

    print("\nTournament 2 (multiple)")
    print(
        "  [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")

    aquabub = acf.create_base()
    sproutling = hcf.create_base()
    shiftling = tcf.create_base()

    print("\n* Battle *")
    print(aquabub.describe())
    print("  vs.")
    print(sproutling.describe())
    print("  now fight!")
    print(ex2.NormalStrategy().act(aquabub))
    print(ex2.DefensiveStrategy().act(sproutling))

    print("\n* Battle *")
    print(aquabub.describe())
    print("  vs.")
    print(shiftling.describe())
    print("  now fight!")
    print(ex2.NormalStrategy().act(aquabub))
    print(ex2.AggressiveStrategy().act(shiftling))

    print("\n* Battle *")
    print(sproutling.describe())
    print("  vs.")
    print(shiftling.describe())
    print("  now fight!")
    print(ex2.DefensiveStrategy().act(sproutling))
    print(ex2.AggressiveStrategy().act(shiftling))
