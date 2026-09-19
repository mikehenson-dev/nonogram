# ============================================================
# Lab Activity 01: Nonogram Puzzle
# Name    : ARCALAS, MIKE HENSON D.
# Section : CITCS 1E
# Legend  : .  = blank space      X = solid square
# ============================================================

# Name on the left, section on the right.
# \t inserts a wide blank space to push the section to the right side.
print("ARCALAS, MIKE HENSON D.\t\tCITCS 1E")

# Title of the activity, roughly centered above the grid.
# \n at the end leaves one empty line after the title.
print("Lab Activity 01: Nonogram Puzzle\n")

# ------------------------------------------------------------
# BLANK GRID
# The top numbers are the column clues, the left numbers are the
# row clues. Every square starts out as a dot ( . ).
# ------------------------------------------------------------
print("Blank Grid:")

# Triple quotation marks let one print() display many lines at once.
print("""               3             1 2
           1   1 1   1 3     4 5 2
           1 4 1 3 1 1 1 5 5 1 1 4 3 5 1
           1 2 1 1 5 2 3 5 3 1 1 4 1 3 3
           1 2 1 1 6 8 2 2 4 2 1 1 2 3 6
           ------------------------------
  4 1 3 1 |. . . . . . . . . . . . . . .
  2 3 2 2 |. . . . . . . . . . . . . . .
    2 6 2 |. . . . . . . . . . . . . . .
    1 2 9 |. . . . . . . . . . . . . . .
    1 3 8 |. . . . . . . . . . . . . . .
  1 4 4 1 |. . . . . . . . . . . . . . .
    1 1 2 |. . . . . . . . . . . . . . .
1 1 1 2 1 |. . . . . . . . . . . . . . .
    2 3 3 |. . . . . . . . . . . . . . .
  2 5 2 2 |. . . . . . . . . . . . . . .
  1 4 1 4 |. . . . . . . . . . . . . . .
    6 3 1 |. . . . . . . . . . . . . . .
  2 2 1 2 |. . . . . . . . . . . . . . .
  2 6 1 2 |. . . . . . . . . . . . . . .
  1 1 6 2 |. . . . . . . . . . . . . . .""")

# ------------------------------------------------------------
# SOLVED GRID
# X marks a solid square, . is still a blank space.
# ------------------------------------------------------------
print("\nSolution:")

print("""               3             1 2
           1   1 1   1 3     4 5 2
           1 4 1 3 1 1 1 5 5 1 1 4 3 5 1
           1 2 1 1 5 2 3 5 3 1 1 4 1 3 3
           1 2 1 1 6 8 2 2 4 2 1 1 2 3 6
           ------------------------------
  4 1 3 1 |. . X X X X . X . X X X . X .
  2 3 2 2 |. X X . . . X X X . X X . X X
    2 6 2 |. X X . X X X X X X . . X X .
    1 2 9 |. X . X X . X X X X X X X X X
    1 3 8 |. X . X X X . X X X X X X X X
  1 4 4 1 |X . X X X X . . X X X X . . X
    1 1 2 |. . . . X . X . . . X X . . .
1 1 1 2 1 |X . X . . X . X X . X . . . .
    2 3 3 |. . . . X X . X X X . X X X .
  2 5 2 2 |. X X . X X X X X . X X . X X
  1 4 1 4 |. X . . X X X X . X . X X X X
    6 3 1 |. . . X X X X X X . X X X . X
  2 2 1 2 |X X . . X X . . X . . . . X X
  2 6 1 2 |. X X . X X X X X X . X . X X
  1 1 6 2 |X . . X . X X X X X X . . X X""")
