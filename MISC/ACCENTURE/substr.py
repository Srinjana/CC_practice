# A string is said to be a substring of another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what’s the longest string that can be constructed such that it is a substring of both?

# For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can’t rearrange characters and ABCD ≠ ABDC.


# Input Format

# There is one line with two space-separated strings, s1 and s2 .

# Output Format

# Print the length of the longest string s, such that is a child of both s1 and s2.

# Sample Input

# HARRY

# SALLY

# Sample Output

# 2

def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    # """Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]"""

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


def commonChild(s1, s2):
    common_letters = set(s1) & set(s2)

    if (not bool(common_letters)):
        return 0

    s1_filt = "".join([x for x in s1 if x in common_letters])
    s2_filt = "".join([x for x in s2 if x in common_letters])

    #return LCSubStr(s1_filt, s2_filt, len(s1_filt), len(s2_filt))
    return lcs(s1, s2)


s1 = input()

s2 = input()

result = commonChild(s1, s2)

print(str(result) + '\n')
