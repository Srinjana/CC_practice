# Given a maximum of four digit to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as input, output its decimal value.
# Input:
# 23GF
# Output
# 10980

input_string = input("Enter base 17 digits: ")
res = int(input_string, 17)
print("OUTPUT")
print (res)