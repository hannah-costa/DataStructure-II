import random

''''''''''''''''''''''''
'''  INSERTIONSORT  '''
''''''''''''''''''''''''


def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


''''''''''''''''''''''''
'''  SELECTIONSORT  '''
''''''''''''''''''''''''


def selectionSort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


''''''''''''''''''''''''
'''    SHELLSORT    '''
''''''''''''''''''''''''


def shellSort(array):
    length = len(array)
    h = 1
    while h < length:
        if 3 * h + 1 < length:
            h = 3 * h + 1
        else:
            break
    while h >= 1:
        for i in range(h, length):
            j = i
            while j >= h and array[j] < array[j - h]:
                array[j], array[j - h] = array[j - h], array[j]
                j -= h
        h = (h - 1) // 3
    return array


''''''''''''''''''''''''
'''    QUICKSORT    '''
''''''''''''''''''''''''


def quickSort(array, start, end):
    if start < end:
        pivot = randomPartition(array, start, end)

        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

    return array


def partition(array, start, end):
    pivot = end
    i = start - 1
    j = start
    while j < end:
        if array[j] <= array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[pivot], array[i + 1] = array[i + 1], array[pivot]

    # returns the new pivot position:
    return i + 1


def randomPartition(array, start, end):
    pivot = random.randint(start, end)
    array[pivot], array[end] = array[end], array[pivot]
    return partition(array, start, end)


''''''''''''''''''''''''
'''   QUICKSORT P.I. '''
''''''''''''''''''''''''


def quickSort(array, start, end, L=-1):
    if start < end:
        pivot = randomPartition(array, start, end)

        if pivot - 1 - start <= L:
            insertionSort(array[start:pivot - 1])
        else:
            quickSort(array, start, pivot - 1)
        if end - pivot + 1 <= L:
            insertionSort(array[pivot + 1:end])
        else:
            quickSort(array, pivot + 1, end)

    return array


def partition(array, start, end):
    pivot = end
    i = start - 1
    j = start
    while j < end:
        if array[j] <= array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[pivot], array[i + 1] = array[i + 1], array[pivot]

    # returns the new pivot position:
    return i + 1


def randomPartition(array, start, end):
    pivot = random.randint(start, end)
    array[pivot], array[end] = array[end], array[pivot]
    return partition(array, start, end)


''''''''''''''''''''''''
'''    MERGESORT    '''
''''''''''''''''''''''''


def mergeSort(array, left, right, arrayAux=None):
    if arrayAux is None:
        arrayAux = array[:]
    if left < right:
        half = (right - left) // 2
        mergeSort(array, left, half, arrayAux)
        mergeSort(array, half + 1, right, arrayAux)
        merge(array, left, right, arrayAux)

    return array


def merge(array, left, right, arrayAux):
    leftEnd = right-1
    auxPos = left

    while left <= leftEnd and right <= ri


# durand
'''
def mergeSort(array):
    if len(array) > 1:
        half = len(array) // 2
        arrayLeft = mergeSort(array[:half])
        arrayRight = mergeSort((array[half:]))

        i, j, k = 0, 0, 0
        while i < len(arrayLeft) and j < len(arrayRight):
            if arrayLeft[i] < arrayRight[j]:
                array[k] = arrayLeft[i]
                i += 1
                k += 1
            else:
                array[k] = arrayRight[j]
                j += 1
                k += 1

        while i < len(arrayLeft):
            array[k] = arrayLeft[i]
            i += 1
            k += 1

        while j < len(arrayRight):
            array[k] = arrayRight[j]
            j += 1
            k += 1

        return array

    else:
        return array
'''

if __name__ == '__main__':
    array = [6, 1, 3, 4, 3, 2, 9, 3]
    # print(insertionSort(array))
    # print(selectionSort(array))
    # print(shellSort(array))
    # print(quickSort(array, 0, 7)) # quicksort
    # print(quickSort(array, 0, 7, 2)) # quicksort with partial insertion
    # print(mergeSort(array, 0, 7)
    print(mergeSort(array))
