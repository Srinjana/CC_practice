# One programming language has the following keywords that cannot be used as identifiers:
# break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var
# Write a program to find if the given word is a keyword or not

# Input  # 1:
# defer

# Output: 
# defer is a keyword

keywords = ['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']

string = input("Enter the keyword: ").lower()

if string in keywords:
    print( string + " is a keyword." )
else:
    print(string + " is not a keyword.")