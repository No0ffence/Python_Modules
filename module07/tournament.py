from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, DefensiveStrategy,
                 AggressiveStrategy, BattleStrategy, InvalidStrategyError)


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for index, current in enumerate(opps):
        current_factory, current_strategy = current
        current_character = current_factory.create_base()
        for opp in opps[index + 1:]:
            opp_strategy = opp[1]
            opp_character = opp[0].create_base()
            print("\n* Battle *")
            print(current_character.describe())
            print("vs")
            print(opp_character.describe())
            print("now fight!")
            try:
                current_strategy.act(current_character)
                opp_strategy.act(opp_character)
            except InvalidStrategyError as e:
                print(e)


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_str = NormalStrategy()
    aggressive_str = AggressiveStrategy()
    defensive_str = DefensiveStrategy()

    print('''
Tournament 0 (basic)
[ (Flameling+Normal), (Healing+Defensive) ]
*** Tournament ***
2 opponents involved
    ''')
    lst = [(flame_factory, normal_str), (healing_factory, defensive_str)]
    battle(lst)

    print('''
Tournament 1 (error)
[ (Flameling+Aggressive), (Healing+Defensive) ]
*** Tournament ***
2 opponents involved
    ''')
    lst = [(flame_factory, aggressive_str), (healing_factory, defensive_str)]
    battle(lst)

    print('''
Tournament 2 (multiple)
[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
*** Tournament ***
3 opponents involved
    ''')
    lst = [(aqua_factory, normal_str), (healing_factory, defensive_str),
           (transform_factory, aggressive_str)]
    battle(lst)


if __name__ == "__main__":
    main()
