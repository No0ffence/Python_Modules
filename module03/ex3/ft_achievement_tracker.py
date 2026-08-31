import random


class Player:
    achievements = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor',
                    'Master Explorer', 'Treasure Hunter', 'Unstoppable',
                    'First Steps', 'Collector Supreme', 'Untouchable',
                    'Sharp Mind', 'Boss Slayer'}

    def __init__(self, player_name: str) -> None:
        self._name = player_name
        self._achieves = self.gen_player_achievements()

    def gen_player_achievements(self) -> set[str]:
        picked = set(random.sample(
            list(self.achievements),
            random.randrange(1,
                             len(self.achievements))))
        return picked

    def print_players_ach(self) -> None:
        print(f"Player {self._name}: {self._achieves}")

    def get_achieves(self) -> set[str]:
        return self._achieves

    def get_name(self) -> str:
        return self._name

    def get_missing(self) -> set[str]:
        return set.difference(self.achievements, self._achieves)


def main() -> None:
    print("=== Achievement Tracker System ===")
    player_one = Player("Alice")
    player_one.print_players_ach()
    player_two = Player("Bob")
    player_two.print_players_ach()
    player_three = Player("Charlie")
    player_three.print_players_ach()
    player_four = Player("Dylan")
    player_four.print_players_ach()

    distinct_achievements = set.union(
        player_one.get_achieves(),
        player_two.get_achieves(),
        player_three.get_achieves(),
        player_four.get_achieves()
    )
    print(f"\nAll distinct achievements: {distinct_achievements}")

    common_achievements = set.intersection(
        player_one.get_achieves(),
        player_two.get_achieves(),
        player_three.get_achieves(),
        player_four.get_achieves()
    )
    only_first = set.difference(
        player_one.get_achieves(),
        player_two.get_achieves(),
        player_three.get_achieves(),
        player_four.get_achieves()
    )
    only_second = set.difference(
        player_two.get_achieves(),
        player_one.get_achieves(),
        player_three.get_achieves(),
        player_four.get_achieves()
    )
    only_three = set.difference(
        player_three.get_achieves(),
        player_two.get_achieves(),
        player_one.get_achieves(),
        player_four.get_achieves()
    )
    only_four = set.difference(
        player_four.get_achieves(),
        player_two.get_achieves(),
        player_three.get_achieves(),
        player_one.get_achieves()
    )
    print(f"\nCommon achievements: {common_achievements}")

    print(f"\nOnly {player_one.get_name()} has: {only_first}")
    print(f"Only {player_two.get_name()} has: {only_second}")
    print(f"Only {player_three.get_name()} has: {only_three}")
    print(f"Only {player_four.get_name()} has: {only_four}")

    print(f"\n{player_one.get_name()} is missing: {player_one.get_missing()}")
    print(f"{player_two.get_name()} is missing: {player_two.get_missing()}")
    print(
        f"{player_three.get_name()} is missing: {player_three.get_missing()}")
    print(f"{player_four.get_name()} is missing: {player_four.get_missing()}")


if __name__ == "__main__":
    main()
