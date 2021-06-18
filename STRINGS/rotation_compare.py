# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
# (eg given s1=ABCD and s2=CDAB, return true, given s1=ABCD, and s2=ACBD, return false)

def areRotations(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return 0

    # Create a temp staring with value str1.str1
    temp = str1 + str1

    # see if str2 is substring of temp

    if (temp.count(str2) > 0):
        return 1
    else:
        return 0


# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

# string1 = "AABBA"
# string2 = "BABBA"
  
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")
