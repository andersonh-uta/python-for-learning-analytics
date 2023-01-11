"""
https://adventofcode.com/2021/day/10

There's a "language" that consists entirely of brackets:
(, ), [, ], {, }, <, and >.

Every bracket must be paired with its closing bracket, but multiple
other brackets may come between.  E.g.:
    ([]) is valid
    ([) is NOT valid--the [ was not closed before the ( was closed.

Incorrect closing brackets are worth "points" based on what the bracket is.  Only the
first one on a line counts.
    ) 3 points
    ] 57 points
    } 1197 points
    > 25137 points

What is the sum of the error scores for each line in the input file?
"""
