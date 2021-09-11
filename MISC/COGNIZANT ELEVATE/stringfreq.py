# Problem Statement: Seema loves working with strings. She always tries to perform some operations on strings. One day she decided to find the frequencies of each of the characters in a given string but she found some difficulty in doing this so she needs your help. Help Seema by finding the frequencies of each of the characters in a given string. The input string contains only lowercase letters. The output string should contain a letter followed by its frequency, in alphabetical order (from a to z).

 

# Input Specification:

# input1: the input string
# Output Specification:

# Return a string representing the frequency counts of characters in the input string.
 

# Test Cases:

# Example 1:

# Input: str = “aabccccddd” 
# Output: a2b1c4d3 
# Example 2:

# Input: str = “prepinsta” 
# Output: a1e1i1n1p2r1s1t1

MAX = 26

def compressString(s, n):

    # To store the frequency of the characters
    freq = [0] * MAX

    # Update the frequency array
    for i in range(n):
        freq[ord(s[i]) - ord('a')] += 1

    # Print the frequency in alphatecial order
    for i in range(MAX):

        # If the current alphabet doesn't appear in the string
        if (freq[i] == 0):
            continue

        print((chr)(i + ord('a')), freq[i], end=" ")


# Driver code
if __name__ == "__main__":

    s = input()
    n = len(s)

    compressString(s, n)
