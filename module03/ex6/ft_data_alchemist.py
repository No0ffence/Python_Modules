import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_list}")

    all_capitalized = [x.capitalize() for x in initial_list]
    print(f"New list with all names capitalized: {all_capitalized}")

    second_list = [x for x in initial_list if x == x.capitalize()]
    print(f"New list of capitalized names only: {second_list}")

    players = {name: random.randrange(1, 1000)
               for name in all_capitalized}
    print(f"Score dict: {players}")

    avg = round(sum(players.values()) / len(players), 2)
    print(f"Score average is {avg}")

    high_scores = {k: v for k, v in players.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
