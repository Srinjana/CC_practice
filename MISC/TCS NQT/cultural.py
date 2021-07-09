# Our hoary culture had several great persons since time immemorial and king vikramaditya’s nava ratnas(nine gems) belongs to this ilk.They are named in the following shloka:


# Among these, Varahamihira was an astrologer of eminence and his book Brihat Jataak is recokened as the ultimate authority in astrology. He was once talking with Amarasimha, another gem among the nava ratnas and the author of Sanskrit thesaurus, Amarakosha. Amarasimha wanted to know the final position of a person, who starts from the origin 0 0 and travels per following scheme.


# He first turns and travels 10 units of distance
# His second turn is upward for 20 units
# Third turn is to the left for 30 units
# Fourth turn is the downward for 40 units
# Fifth turn is to the right(again) for 50 units
# … And thus he travels, every time increasing the travel distance by 10 units

# Constraints:
# 2 <= n <= 1000

# Input:
# 3
# Output
# -20 20

# number of iterations 
n = int(input())
x, y = 0, 0
c = 'R'
dist = 10

for i in range(n):

    if c == 'R':
        x = x + dist
        dist = 2 * dist
        c = 'U'

    elif c == 'U':
        y = y + dist
        c = 'L'
        dist = dist + 10

    elif c == 'L':
        x = x - dist
        c = 'D'
        dist = dist + 10

    elif c == 'D':
        y = y - dist
        c = 'AGAIN'
        dist = dist + 10
    
    elif c == 'AGAIN':
        x = x + dist
        c = 'R'
        dist = dist + 10
    else:
        break

print(x, y)
