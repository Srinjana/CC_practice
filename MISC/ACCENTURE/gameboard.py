# Two players are playing a game with a starting number of tokens. Player names are Mayur(P1) and Divyanshu(P2). Mayur always plays first, and the two players move in alternating turns. The game’s rules are as follows:
# In a single move, a player can remove either 2,3  or5 tokens  from the game board.
# If a player is unable to make a move, that player loses the game
# Given the starting number of tokens, find and print the name of the winner. Mayur is named First and Divyanshu is named Second. Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.

# For example, if n = 4, Mayur can make the following moves:

# Mayur removes 2 tokens leaving 2. Divyanshu will then remove 2 tokens and win.
# Mayur removes 3 tokens leaving 1. Divyanshu cannot move and loses.
# Mayur would make the second play and win the game.

# Input Format
# The first line contains an integer t, the number of test cases.
# Each of the next t lines contains an integer n, the number of tokens in a test case.
# Output Format
# On a new line for each test case, print First if the first player is the winner. Otherwise print Second.

# Sample Input
# 8
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 10

# Sample Output
# Second
# First
# First
# First
# First
# First
# Second
# First


def gameOfTokens(n):
    if n%7 == 1 or n%7 == 0:
        return 'Second'
    else:
        return 'First'

t = int(input())
tokens = []
result = []
for a in range(t):
    tokens.append(input())
for n in tokens:
    result.append(gameOfTokens(int(n)))
for i in result:
    print(i)