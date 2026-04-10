import ex0
import ex1
import ex2


if __name__ == "__main__":
    hcf = ex1.HealingCreatureFactory()
    sproutling = hcf.create_base()
    def_s = ex2.strategy.DefensiveStrategy()
    print(def_s.act(sproutling))

    tcf = ex1.TransformCreatureFactory()
    shiftling = tcf.create_base()
    agr_s = ex2.AggressiveStrategy()
    print(agr_s.act(shiftling))
    try:
        print(agr_s.act(sproutling))
    except Exception as e:
        print(e)
