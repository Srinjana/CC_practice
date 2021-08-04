# Find the second most frequent character in a string.


def getSecondMostFreq(str):
    NO_OF_CHARS = 256
    count = [0]* NO_OF_CHARS
    for i in range(len(str)):
        count[ord(str[i])] += 1

    first, second = 0, 0

    for i in range(NO_OF_CHARS):

        # If current element is smaller
        # than first then update both
        # first and second
        if count[i] > count[first]:

            second = first
            first = i
        
        # If count[i] is in between
        # first and second
        # then update second */
        elif (count[i] > count[second] and count[i] != count[first]):

            second = i
        
    return chr(second)

if __name__ == "__main__":

    str = input("Enter the string: ")

    # function calling
    res = getSecondMostFreq(str)
    if res != '\0':
        print("Second most frequent char is", res)
    else:
        print("No second most frequent character")
