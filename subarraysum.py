n=int(input("Enter the number of elements: "))
arr=list(map(int, input("Enter the elements of the array: ").split()))
print(arr)
target=int(input("Enter the target sum: "))
def subarray_sum(a, target):
    n = len(a)
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += a[j]
            if curr_sum == target:
                return i+1, j+1
    return -1, -1

# arr=[1,2,3,7,5]
print(subarray_sum(arr,target))
