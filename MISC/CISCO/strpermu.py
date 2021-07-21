# Given a string S. The task is to print all permutations of a given string.

def perms(string, i=0):

    n = len(string)
    if i == n:
        print("".join(string))
    for j in range(i, n):

        words = [c for c in string]
        words[i], words[j] = words[j], words[i]

        perms(words, i+1)


string = (input("Enter the string: "))
perms(string)
