def binary_search(element, arrs):
    low = 0
    high = len(arrs) - 1
    while(low <= high):
        middle = (low + high) // 2
        if arrs[middle] == element:
            return middle
        else:
            if arrs[middle] < element:
                low = middle + 1
            elif arrs[middle] > element:
                high = middle - 1
    return -1


print(binary_search(element=8, arrs=[1, 3, 4, 6, 8, 9]))  
