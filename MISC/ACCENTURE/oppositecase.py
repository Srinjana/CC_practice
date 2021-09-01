# Given a string, convert the characters of the string into opposite case, i.e. if a character is lower case then convert it into upper case and vice-versa.


def convertOpposite(str):
    ln = len(str)

    # Conversion according to ASCII values
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':

            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) - 32)

        elif str[i] >= 'A' and str[i] <= 'Z':

            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) + 32)


# Driver code
if __name__ == "__main__":
    str = input()
    str = list(str)

    # Calling the Function
    convertOpposite(str)

    str = ''.join(str)
    print(str)
