"""
https://adventofcode.com/2022/day/1

Elves are carrying food with different amounts of calories.
What each elf is carrying is listed as a set of consecutive numbers;
each elf is separated by a blank line.

Part 1: what is the maximum number of calories carried by any one elf?

Part 2: how many calories are carried by the top 3 elves, combined?
"""


def calories_per_elf():
    calories = open("inputs/2022_day_1").readlines()
    total_calories = [0]
    for i in calories:
        if i == "\n":
            total_calories.append(0)
        else:
            total_calories[-1] += int(i)

    return total_calories


def calories_per_elf_functional():
    elves = [
        sum(map(int, i.strip().split("\n"))) for i in open("inputs/2022_day_1").read().split("\n\n")
    ]
    return elves


if __name__ == "__main__":
    calories = calories_per_elf()
    print(max(calories))
    print(sum(sorted(calories)[-3:]))

    # calories = calories_per_elf_functional()
    # print(max(calories))
    # print(sum(sorted(calories)[-3:]))
