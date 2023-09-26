def linearSearch(array, x):
    # Going through array sequencially

    for i in range(0, len(array)):
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9]
x = 1
print(linearSearch(array, x))
