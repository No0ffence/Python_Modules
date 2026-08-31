def rec_print(i, days):
    print(f"Day {i}")
    if i == days:
        print("Harvest time!")
        return
    rec_print(i + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    rec_print(1, days)
