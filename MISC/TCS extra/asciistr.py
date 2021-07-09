# In the Byteland country, a string S is said to super ASCII string if and only if the count of each character in the string is equal to its ASCII value. In the Byteland country ASCII code of ‘a’ is 1, ‘b’ is 2, …, ‘z’ is 26. The task is to find out whether the given string is a super ASCII string or not. If true, then print “Yes” otherwise print “No”.

# Examples:

# Input: S = “bba”
# Output: Yes
# Explanation:
# The count of character ‘b’ is 2 and the ASCII value of ‘b’ is also 2.
# The count of character ‘a’ is 1. and the ASCII value of ‘a’ is also 1.
# Hence, string “bba” is super ASCII String.

# Input: S = “ssba”
# Output: No
# Explanation:
# The count of character ‘s’ is 2 and the ASCII value of ‘s’ is 19.
# The count of character ‘b’ is 1. and the ASCII value of ‘b’ is 2.
# Hence, string “ssba” is not a super ASCII String.

def checkSuperASCII(str):

    freq = [0 for i in range(26)]

    for i in range (len(str)):
        # AscASCIIii value of the
        # current character
        index = ord(str[i]) - 97 + 1

        freq[index - 1] += 1
    
    # Traverse the string
    for i in range(len(str)):

        # ASCII value of the current
        # character
        index = ord(str[i]) - 97 + 1

        # Check if the frequency of
        # each character in string
        # is same as ASCII code or not
        if (freq[index - 1] != index):
            print("No")
            return

    # Else print "Yes"
    print("Yes")

# Driver Code
if __name__ == '__main__':

    # Given string S
    s = input("Enter str: ")

    # Function Call
    checkSuperASCII(s)
