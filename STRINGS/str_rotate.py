# input is a dictionary type string where every string is associated with a number, if the sum of square of the digits is even then the string rotates right by one position, and if sum of square of digits is odd, the string rotatoes by two poitions
# eg input erft:235, ghtdf:6481
# Author @Srinjana

# PARSING THE INPUT
entries = input().split(',')
strings = []
digits = []

for i in entries:
    s1, d1 = i.split(':')
    strings.append(s1)
    digits.append(d1)

# STRING ROTATION FUNCTION
def rotatoPotato (s1, d1):
    d1 = list(str(d1))
    s2 = 0
    for i in d1:
        s2 += int(i)**2
    if s2%2 == 0:
        return s1[-1:]+s1[:-1]  # single place rotation
    else:
        return s1[2:]+s1[:2] # two places rotation

# CALLING THE FUNCTION IN MAIN FOR EXECUTION
for i in range(len(digits)):
    print(rotatoPotato(strings[i],digits[i]))
