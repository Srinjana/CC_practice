# Write a program to enter a string and print all possible permutations of that string.
# A permutation, also called an “arrangement number” or “order, ” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

# Below are the permutations of string CAT.
# ATC ACT TAC TCA CTA CAT

def perms(a,l,r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            perms(a, l+1, r)
            a[l], a[i] = a[i], a[l]
            
stir = input()
n = len(stir)
a = list(stir)
res = perms(a, 0, n-1)
