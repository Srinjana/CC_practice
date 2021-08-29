# Problem Statement

# You are required to input the size of the matrix then the elements of matrix, then you have to divide the main matrix in two sub matrices(even and odd) in such a way that element at 0 index will be considered as even and element at 1st index will be considered as odd and so on. then you have sort the even and odd matrices in ascending order then print the sum of second largest number from both the matrices

# Example

# enter the size of array: 5
# enter element at 0 index: 3
# enter element at 1 index: 4
# enter element at 2 index: 1
# enter element at 3 index: 7
# enter element at 4 index: 9
# Sorted even array: 1 3 9
# Sorted odd array: 4 7


array = []
evenArr = []
oddArr = []
n = int(input("Enter the size of array:"))

for i in range(0, n):
    number = int(input("Enter Element at {} index:".format(i)))
    array.append(number)
    
    if i % 2 == 0:
        evenArr.append(array[i])
    else:
        oddArr.append(array[i])

evenArr = sorted(evenArr)
print("Sorted Even Array:", evenArr[0:len(evenArr)])
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])
print(evenArr[1] + oddArr[1])
