# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

inputstr = input("Enter string with words seperated by dots: ")
lstowords = inputstr.split(".")
print (lstowords)

revlst = lstowords[::-1]

ans = (".".join(revlst))
print(ans)
