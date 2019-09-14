def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


# def mergeSort(array):


# def quickSort(array):

# def shellSort(array):

def selectionSort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


if __name__ == '__main__':
    array = [6, 1, 3, 4, 3, 2, 9, 3]
    # print(insertionSort(array))
    print(selectionSort(array))
