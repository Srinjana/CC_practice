# Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.
# Input:
# N = 7, K = 23
# A[] = {10, 2, 3, 4, 5, 7, 8}
# Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
# Explanation: Sum of 2, 3, 8, 10 = 23,
# sum of 2, 4, 7, 10 = 23 and sum of 3,
# 5, 7, 8 = 23.

# A sorting based solution to print all combination
# of 4 elements in A[] with sum equal to X
def find4Numbers(A, n, X):

	# Sort the array in increasing order
	A.sort()

	# Now fix the first 2 elements one by
	# one and find the other two elements
    #LEAVING PROVISIONS FOR left and right vars in the end [i,j,left, right]
	for i in range(n - 3):
		for j in range(i + 1, n - 2):

			# Initialize two variables as indexes
			# of the first and last elements in
			# the remaining elements
			left = j + 1
			right = n - 1

			# To find the remaining two elements,
			# move the index variables (l & r)
			# toward each other.
			while (left < right):
				if(A[i] + A[j] + A[left] + A[right] == X):
				    print(A[i], ",", A[j], ",",
                                    A[left], ",", A[right])
				    left += 1
				    right -= 1

				elif (A[i] + A[j] + A[left] + A[right] < X):
					left += 1
				else:  # A[i] + A[j] + A[l] + A[r] > X
					right -= 1


# Driver Code
if __name__ == "__main__":

	# A = [10, 2, 3, 4, 5, 7, 8]
	# X = 23
	# n = len(A)
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        i = int(input())
        a.append(i)
	find4Numbers(a, n, k)

