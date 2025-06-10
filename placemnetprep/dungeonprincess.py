arr=((-2,-3,3,),
     (-5,-10,1),
     (10,30,-5))
def safest(arr):
    lowest=0


    print("RD:", calculateRD(arr))
    print("DR:", calculateDR(arr))
    print("Diag:", calculateDiagonal(arr))
    lowest=max(calculateDiagonal(arr), calculateRD(arr), calculateDR(arr))
    return lowest

def calculateRD(arr):
    lowe=0
    for i in range(3):
        lowe=lowe+arr[0][i]
    for i in range(1,3):

        lowe=lowe+arr[i][2]
    return lowe
def calculateDR(arr):
    lowe=0
    for i in range(3):
        # print("     ", lowe, arr[i][0])
        lowe=lowe+arr[i][0]
    for i in range(1,3):
        # print("     ", lowe, arr[2][i])
        lowe=lowe+arr[2][i]
    return lowe
def calculateDiagonal(arr):
    lowe=0
    for i in range(3):
        lowe+=arr[i][i]
    return lowe
print(safest(arr))