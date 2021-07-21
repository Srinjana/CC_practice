# Given a number N, swap the two nibbles in it and find the resulting number.
# A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.
# Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte(or 8 bits). The two nibbles are(0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.


# Example 1:

# Input:
# N = 100
# Output:
# 70
# Explanation:
# 100 in binary is 01100100,
# two nibbles are(0110) and (0100)
# If we swap the two nibbles, we get
# 01000110 which is 70 in decimal

def nibbleswap(decimal):
    return ( (decimal & 0x0F)<<4 | (decimal & 0xF0)>>4 )


decimal = int(input("Enter number: "))
res = nibbleswap(decimal)
print(res)

