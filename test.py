def reverse_array(array):
    j = len(arr) - 1
    for i in range(len(array)):
        if j > i:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j -= 1
    print(array)


arr = [2, 8, 7, 6, 5]
reverse_array(arr)
