# Problem Statement:  Johnny was absent in his English class when the vowel topic was taught by the teacher. His English teacher gave him two strings and told him to find the length of the longest common subsequence which contains only vowels, as a punishment for not attending English class yesterday.

# Help Jhonny by writing a code to find find the length of the longest common subsequence.

# Input Specification:

# input1: First string is given by his teacher
# input2: Second-string given by his teacher.
# Output Specification:

# Return the length of the longest common subsequence which contains only vowels.

# Test Cases:

# Example 1:

# input1: aieef
# input2: klaief
# Output: 3


def isVowel(x):
    return (x == 'a' or x == 'e'or x == 'i' or x == 'o' or x == 'u')


def longestVowelSubsequence(str):

    answer = ""
    n = len(str)

    for i in range(n):

        if (isVowel(str[i])):
            answer += str[i]

    return answer


s1 = input()
s2 = input()
print(longestVowelSubsequence(s1))
print(longestVowelSubsequence(s2))
