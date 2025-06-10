# Problem Statement – An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:
#
# 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
# 2nd data, Total number of wheels = W
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.
V=input("Enter the total number of vehicles (two-wheeler + four-wheeler): ")
W=input("Enter the total number of wheels: ")

V = int(V)
W = int(W)

def calculate_vehicles(V, W):
    # x + y = V
    # 4x + 2y = W
    # y=v-x
    # 4x + 2(v - x) = W
    # 4x + 2v - 2x = W
    # 2x + 2v = W
    # 2x = W - 2v
    # x = (W - 2 * V) / 2
    # # Using substitution method to solve the equations
    fw= (W - 2 * V) // 2
    tw = V - fw
    return fw, tw
fw, tw = calculate_vehicles(V, W)
print(f"Number of four-wheelers: {fw}")
print(f"Number of two-wheelers: {tw}")