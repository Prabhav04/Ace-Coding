# Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.
#
# Note : 1st element of the array should be considered in the count of the result.
#
# For example,
# Arr[]={7,4,8,2,9}
# As 7 is the first element, it will consider in the result.
# 8 and 9 are also the elements that are greater than all of its previous elements.
# Since total of  3 elements is present in the array that meets the condition
n= int(input("Enter the size of the array: "))
Arr = list(map(int, input("Enter the elements of the array: ").split()))

def count_greater_elements(Arr):
    count = 1  # Start with the first element
    max=Arr[0]
    for i in range(1, len(Arr)):
        if Arr[i] > max:
            count += 1
            max = Arr[i]
    return count

result = count_greater_elements(Arr)
print("Count of elements greater than all prior elements:", result)