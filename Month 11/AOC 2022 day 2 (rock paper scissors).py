"""
https://adventofcode.com/2022/day/2

You're in a Rock Paper Scissors tournament.  Youv'e been given a cheat
sheet of what moves to take, but it's been enciphered, and you don't know
what corresponds to what.

Point are scored as follows:
    If you lose, you get 0 points.
    Draw: 3 points.
    Win: 6 points.

    You played Rock: 1 point
    You played Paper: 2 points
    You played Scissors: 3 points

If everything goes perfectly, how many points do you score?

The input file is listed as:
    [other player's move][space][your enciphered move]

Other player's moves:
    A = rock
    B = paper
    C = scissors
"""
import itertools

def check_points(them, me, hypothesis):
    """
    For a given hypothesis of how X/Y/Z map to rock/paper/scissors,
    and for an opponent's move, calculate the total points you'd
    score in that round.
    """
    # Convert the encoded move to "rock", "paper", or "scissors"
    # depending on the current hypothesis.
    me = hypothesis.get(me, me)

    # Calculate the points based just on what move I chose
    total_points = 0
    move_choice_points = {"rock": 1, "paper": 2, "scissors": 3}
    total_points += move_choice_points[me]

    # calculate points based on who won
    match (them, me):
        case ("rock", "rock"):
            total_points += 3
        case ("rock", "paper"):
            total_points += 6
        case ("rock", "scissors"):
            total_points += 0
        case ("paper", "rock"):
            total_points += 0
        case ("paper", "paper"):
            total_points += 3
        case ("paper", "scissors"):
            total_points += 6
        case ("scissors", "rock"):
            total_points += 6
        case ("scissors", "paper"):
            total_points += 0
        case ("scissors", "scissors"):
            total_points += 3

    return total_points


moves = open("inputs/2022_day_2").readlines()
moves = [i.strip().split() for i in moves]
move_names = {"A": "rock", "B": "paper", "C": "scissors"}
moves = [(move_names[i], j) for i, j in moves]

hypotheses = [
    dict(zip(["X", "Y", "Z"], i)) for i in itertools.permutations(["rock", "paper", "scissors"])
]
# A Y
# B X
# C Z
test_moves = [
    ("rock", "paper"),
    ("paper", "rock"),
    ("scissors", "scissors")
]
print(sum(
    check_points(i, j, {"X": "rock", "Y": "paper", "Z": "scissors"})
    for i,j in moves
))


# Part 2
def check_points_part_2(them, me):
    total_points = 0
    match (them, me):
        case ("rock", "X"):
            # I play scissors and lose
            total_points += 3
        case ("rock", "Y"):
            # play rock and draw
            total_points += 4
        case ("rock", "Z"):
            # play paper and win
            total_points += 8
        case ("paper", "X"):
            # play rock and lose
            total_points += 1
        case ("paper", "Y"):
            # play paper and draw
            total_points += 5
        case ("paper", "Z"):
            # play scissors and win
            total_points += 9
        case ("scissors", "X"):
            # play paper and lose
            total_points += 2
        case ("scissors", "Y"):
            # scissors and draw
            total_points += 6
        case ("scissors", "Z"):
            # rock and win
            total_points += 7
    return total_points

print(sum(check_points_part_2(i, j) for i,j in moves))
