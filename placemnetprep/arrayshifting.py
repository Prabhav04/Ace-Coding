
def shift_array_right(arr, k):
    n=len(arr)
    k= k % n  # Handle cases where k is greater than n
    if k == 0:
        return arr  # No shift needed
    return arr[-k:] + arr[:-k]

def shift_array_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    if k == 0:
        return arr  # No shift needed
    return arr[k:] + arr[:k]


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    k= int(input().strip())
    shifted_array = shift_array_right(arr, k)
    shifted_arrayleft = shift_array_left(arr, k)
    print(" ".join(map(str, shifted_array)))
    print(" ".join(map(str, shifted_arrayleft)))

