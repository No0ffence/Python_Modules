import sys


def check_arg(arg: str) -> int:
    num = int(arg)
    return num


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ...")
        return None
    for arg in sys.argv[1:]:
        try:
            score = check_arg(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if len(scores) < 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    return None


if __name__ == "__main__":
    main()
