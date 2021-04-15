# input a string of comma seperated numbers . Considering 5 always comes before 8, Add all numbers tht do not lie between 5 and 8 and again concatenate all the numbers that lie between 5 and 8 in the given question. Add the two sums and return the final output
# Author @Srinjana


input_stream = list(map(int, input().split(',')))

num1 =sum(input_stream[: input_stream.index(5)]) + sum(input_stream[input_stream.index(8) + 1 :])

midlist = input_stream[input_stream.index(5) : input_stream.index(8) + 1]

num2 = ""

for i in midlist:
    num2 += str(i)

print (int(num1 + (int(num2))))
