
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
# shift a matrix to the right and left by k positions
def shift_matrix_right(matrix, k):
    return [shift_array_right(row, k) for row in matrix]
def shift_matrix_left(matrix, k):
    return [shift_array_left(row, k) for row in matrix]

if __name__ == '__main__':


    arr = [1,2,4,5,6,7,8,9]
    matrix= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k=5
    # Shift the array to the right and left by k positions
    shifted_array = shift_array_right(arr, k)
    shifted_arrayleft = shift_array_left(arr, k)
    shifted_matrix = shift_matrix_right(matrix, k)
    shifted_matrixleft = shift_matrix_left(matrix, k)
    print(" ".join(map(str, shifted_array)))
    print(" ".join(map(str, shifted_arrayleft)))
    for row in shifted_matrix:
        print(" ".join(map(str, row)))
    for row in shifted_matrixleft:
        print(" ".join(map(str, row)))

