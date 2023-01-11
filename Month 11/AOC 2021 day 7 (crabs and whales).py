"""
https://adventofcode.com/2021/day/7

There are a bunch of crabs who need to move along a line.  Given their
starting positions, what position could they move to that would require
the least *total distance traveled*, summed up over all the crabs?

Part 2: same thing, but now what point minimizes the sum of the squared distances.
"""
import statistics

crab_positions = list(map(int, open("inputs/2021_day_7").read().split(",")))
print(crab_positions)

# find  an integer X such that the total absolute difference between
# X and all other numbers is minimized.
smallest_difference = 1_000_000_000_000_000_000_000
for i in range(min(crab_positions), max(crab_positions) + 1):
    tad = 0
    for crab in crab_positions:
        tad += abs(i - crab)
    smallest_difference = min(tad, smallest_difference)
print(smallest_difference)

median_value = statistics.median(crab_positions)
smallest_difference = sum(abs(median_value - crab) for crab in crab_positions)
print(smallest_difference)


# PART 2
def movement_cost(start, end):
    difference = abs(start - end)
    difference = difference * (difference + 1)
    return difference / 2


smallest_difference = 1_000_000_000_000_000_000_000
for i in range(min(crab_positions), max(crab_positions) + 1):
    tad = 0
    for crab in crab_positions:
        tad += movement_cost(i, crab)
    smallest_difference = min(tad, smallest_difference)
print(smallest_difference)
