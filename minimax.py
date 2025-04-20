
def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    min_sum = sum(arr_sorted[:4])
    max_sum = sum(arr_sorted[-4:])
    return min_sum, max_sum


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    a, b = miniMaxSum(arr)
    print(a, b)


