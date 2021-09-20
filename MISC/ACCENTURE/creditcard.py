
# Problem Statement:
# You and Vaibhav are good friends. Vaibhav received gift cards from his cousin. His cousin is so mischievous that he mixed some forged gift cards with the genuine ones. Now, he wants to verify whether his gift card numbers are valid or not. You happen to be great at programming so he is asking for your help!

# A valid gift card has the following characteristics:

# ► It must start with a 9, 8 or 6 .
# ► It must contain exactly 16 digits.
# ► It must only consist of digits(0-9).
# ► It may have digits in groups of 4, separated by one hyphen “-“.
# ► It must NOT use any other separator like ‘ ‘, ‘_’, etc.
# ► It must NOT have 4 or more consecutive repeated digits.

import re

t = int(input())
numbers = []
results = []

for _ in range(t):
    numbers.append(input())

for num in numbers:

    if (re.match(r'^[986]', num) and (re.match(r'([\d]{4}-){3}[\d]{4}$', num) or re.match(r'[\d]{16}', num)) and not re.search(r'(\d)\1{3,}', num.replace("-", ""))):

        results.append("Valid")

    else:
        results.append("Invalid")

for i in results:

    print(i)
