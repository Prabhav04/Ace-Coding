def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # Slow pointer

    for j in range(1, len(arr)):  # Fast pointer
        if arr[j] != arr[i]:  # Found a new unique element
            i += 1
            arr[i] = arr[j]  # Move the new unique element to its correct place

    return i + 1
