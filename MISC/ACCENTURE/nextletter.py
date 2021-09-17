# Implement the following function: char NextLetter(char chi, char cha)

# The function accepts two characters 'ch1' and 'ch2 as its argument. 'ch1' and 'ch2' are alphabetical letters. Implement the function to find and return the next letter so that distance between ch2 and the next letter is the same as the distance between chi and ch2. While counting distance if you exceed the letter 2 then, count the remaining distance starting from the letter 'a', Distance between two letters is the number of letters between

# them.

# Assumption: All input and output characters are lower case alphabets.

# Example:

# Input:

# ch1: c

# ch2: g

# Output:

# k

# Explanation:

# the distance between the letter 'e' and 'g' is 3 (d, e, f). The next letter with distance 3 from letter 'g' is 'k'. Thus, the output is k.

ch1 = input()
ch2 = input()

diff = abs(ord(ch1) - ord(ch2))
newval = (ord(ch2)+ diff - 25)
print(newval)
print(chr(newval)) 