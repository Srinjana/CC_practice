# Replace Frequent Character

# char * FrequentCharacterReplaced(char *' str, char x)

# The function accepts a string 'str' and a character 'x' as its arguments. You are required to find the most frequent character in string 'str' and replace it with character 'x' across the string, and return the same.


# Note:
# If the frequency of two characters are the same, we have to consider the character with lower ascii value.


# Example:

# Input:
# str: bbadbbababb


# Output:
# ttadttatatt


# Explanation:

# The most frequent character in string 'str' is 'b', replacing 'b' with 't' will form string 'ttadttatatt', hence 'ttadttatatt' is returned.

# Sample Input

# str: jjkdkksjjdjf


def FrequentCharacterReplaced(strl, ch):
    # print(*strl)
    counter = 0
    maxim = strl[0]
    for i in strl:
        cf = strl.count(i)
        if (cf > counter):
            counter = cf
            maxim = i
        # if (cf == maxim):
        #     maxim = 
    return maxim


inp = input()
ch = input()
strl = [d for d in str(inp)]

res = FrequentCharacterReplaced(strl, ch)
# print(res)
print(inp.replace(res, ch))
