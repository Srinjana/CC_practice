# Given an array of positive integers arr[] and a x x, find all unique combinations in arr[] where the x is equal to x. The same repeated number may be chosen from arr[] unlimited number of times. Elements in a combination(a1, a2, …, ak) must be printed in non-descending order. (ie, a1 <= a2 <= … <= ak).
# The combinations themselves must be sorted in ascending order, i.e., the combination with smallest first element should be printed first. If there is no combination possible the print “Empty” (without quotes).

# 1. Sort the array(non-decreasing).
# 2. First remove all the duplicates from array.
# 3. Then use recursion and backtracking to solve
#  the problem.
#   (A) If at any time sub-problem x == 0 then
#       add that array to the result(vector of
#                                      vectors).
#    (B) Else if x is negative then ignore that
#      sub-problem.
#    (C) Else insert the present array in that
#       index to the current vector and call
#        the function with x = x-ar[index] and
#        index = index, then pop that element from
#        current index(backtrack) and call the
#        function with x = x and index = index+1


def combSum(arr, x):
    temp = []
    res = []
    # remove duplicates and Sort the array elements
    arr = sorted(list(set(arr)))
    findNums(res, arr, temp, x, 0)
    return res


def findNums(res, arr, temp, x, index):
    if (x == 0):
        res.append(list(temp))
        return

    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):

        # checking that x does not become negative
        if(x - arr[i]) >= 0:

            # adding element which can contribute to x
            temp.append(arr[i])
            findNums(res, arr, temp, x-arr[i], i)

            # removing element from list (backtracking)
            temp.remove(arr[i])
    



if __name__ == '__main__':
    Arr = []
    ans = []
    Arr = [int(item) for item in input("Enter the list items seperated by a space : ").split()]
    X = int(input("Enter the Maximum Sum: "))

    ans = combSum(Arr, X)

    if (len(ans) == 0):
        print("Empty")

    for i in range(len(ans)):
        print("[", end=' ')

        for j in range(len(ans[i])):
            print(str(ans[i][j])+" ", end=' ')

        print("]", end=' ')


