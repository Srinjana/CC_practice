# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2. And all occurrences of every character in ‘str1’ map to same character in ‘str2’.

# Input:  str1 = "aab", str2 = "xxy"
# Output: True
# 'a' is mapped to 'x' and 'b' is mapped to 'y'.

# Input:  str1 = "aab", str2 = "xyz"
# Output: False
# One occurrence of 'a' in str1 has 'x' in str2 and
# other occurrence of 'a' has 'y'.

# 1) If lengths of str1 and str2 are not same, return false.
# 2) Do following for every character in str1 and str2
#    a) If this character is seen first time in str1, 
#       then current of str2 must have not appeared before.
#       (i) If current character of str2 is seen, return false.
#           Mark current character of str2 as visited.
#       (ii) Store mapping of current characters.
#    b) Else check if previous occurrence of str1[i] mapped
#       to same character. 

MAX_CHARS = 256

def areIsomorphic(str1, str2):
    if (len(str1) != len(str2)):
        return False
    
    # To mark visited characters in str2
    marked = [False] * MAX_CHARS

    # To store mapping of every character from str1 to that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS

    for i in range(len(str2)):
        # if current character of str1 is seen first
        # time in it.
        if map[ord(str1[i])] == -1:

            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(str2[i])] == True:
                return False

            # Mark current character of str2 as visited
            marked[ord(str2[i])] = True

            # Store mapping of current characters
            map[ord(str1[i])] = str2[i]

            # If this is not first appearance of current
            # character in str1, then check if previous
            # appearance mapped to same character of str2
        elif map[ord(str1[i])] != str2[i]:
            return False

    return True


# Driver program

print (areIsomorphic("aab", "xxy"))
print (areIsomorphic("aab", "xyz"))
