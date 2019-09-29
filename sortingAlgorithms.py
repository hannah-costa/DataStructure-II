import random


##-------------------------------##
#         INSERTIONSORT           #
##-------------------------------##
# Starts with element i at index 1 and compares with elements j (sorted part of the array),
# then puts element i in its correct position.
def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


##-------------------------------##
#         SELECTIONSORT           #
##-------------------------------##


def selectionSort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


##-------------------------------##
#           SHELLSORT             #
##-------------------------------##


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


##-------------------------------##
#           QUICKSORT             #
##-------------------------------##
# "Randomized" quicksort. The function randomPartition() gets a random index and switches its position with the last
#  index, using the last element (random) as the pivot.
def quickSort(array, start=0, end=-1):
    if end == -1:
        end = len(array) - 1
    if start < end:
        pivot = randomPartition(array, start, end)

        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

    return array


def partition(array, start, end):
    # uses the last element as the pivot.
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


# Chooses a random index in the array and switches it with the element at the last position,
#  then calls the partition() function.
def randomPartition(array, start, end):
    pivot = random.randint(start, end)
    array[pivot], array[end] = array[end], array[pivot]
    return partition(array, start, end)


##-------------------------------##
#  QUICKSORT - PARTIAL INSERTION  #
##-------------------------------##

def quickSortPI(array, start=0, end=-1, L=-1):
    if end == -1:
        end = len(array) - 1
    if start < end:
        pivot = randomPartition(array, start, end)
        # checks if the partition [start:pivot] is <= L.
        if pivot - 1 - start <= L:
            insertionSort(array[start:pivot - 1])
        else:
            quickSortPI(array, start, pivot - 1)
        # checks if the partition [pivot+1:end] is <= L.
        if end - pivot + 1 <= L:
            insertionSort(array[pivot + 1:end])
        else:
            quickSortPI(array, pivot + 1, end)

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


##-------------------------------##
#   QUICKSORT - FINAL INSERTION   #
##-------------------------------##
def quickSortFI(array, start=0, end=-1, L=-1):
    if end == -1:
        end = len(array) - 1
    if start < end:
        pivot = randomPartition(array, start, end)

        # checks if the partition [start:pivot] is <= L.
        if pivot - 1 - start > L:
            quickSortPI(array, start, pivot - 1)
        # checks if the partition [pivot+1:end] is <= L.
        if end - pivot + 1 > L:
            quickSortPI(array, pivot + 1, end)

        insertionSort(array[start:pivot - 1])
        insertionSort(array[pivot + 1:end])

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


##-------------------------------##
#           MERGESORT             #
##-------------------------------##

def mergeSort(array, left=0, right=-1, arrayAux=None):
    # in the first execution, arrayAux will be none(null). arrayAux will be created and passed as
    # a parameter for the next executions.
    if right == -1:
        right = len(array) - 1
    if arrayAux is None:
        arrayAux = array[:]
    half = left + (right - left) // 2
    # checking whether the received array or subarray has more than one element.
    if left < right:
        mergeSort(array, left, half, arrayAux)
        mergeSort(array, half + 1, right, arrayAux)
        merge(array, left, right, half, arrayAux)

    return array


def merge(array, left, right, half, arrayAux):
    # cur variables will iterate through the array and make comparisons.
    # auxCur indicates the current position in arrayAux.
    leftCur = left
    leftEnd = half
    rightCur = half + 1
    rightEnd = right
    auxCur = left

    # while none of the subarrays have reached an end.
    while leftCur <= leftEnd and rightCur <= rightEnd:
        if array[leftCur] <= array[rightCur]:
            arrayAux[auxCur] = array[leftCur]
            leftCur += 1
        else:
            arrayAux[auxCur] = array[rightCur]
            rightCur += 1
        auxCur += 1

    # only executes when the right subarray has reached an end and the left one hasn't.
    while leftCur <= leftEnd:
        arrayAux[auxCur] = array[leftCur]
        auxCur += 1
        leftCur += 1

    # only executes when the left subarray has reached an end and the right one hasn't.
    while rightCur <= rightEnd:
        arrayAux[auxCur] = array[rightCur]
        auxCur += 1
        rightCur += 1

    # now copy every element of the sorted arrayAux to the original array.
    for i in range(len(array)):
        array[i] = arrayAux[i]


##---------------------------------------##
#      MERGESORT - PARTIAL INSERTION      #
##---------------------------------------##
def mergeSortPI(array, left=0, right=-1, L=-1, arrayAux=None):
    # in the first execution, arrayAux will be none(null). arrayAux will be created and passed as
    # a parameter for the next executions.
    if right == -1:
        right = len(array) - 1
    if arrayAux is None:
        arrayAux = array[:]
    half = left + (right - left) // 2
    # checking whether the received array or subarray has more than one element.
    if left < right:
        if half - left <= L:
            insertionSort(arrayAux[left:half + 1])
        else:
            mergeSort(array, left, half, arrayAux)
        if right - half + 1 <= L:
            insertionSort(arrayAux[half + 1:right])
        else:
            mergeSort(array, half + 1, right, arrayAux)
        merge(array, left, right, half, arrayAux)

    return array


def merge(array, left, right, half, arrayAux):
    # cur variables will iterate through the array and make comparisons.
    # auxCur indicates the current position in arrayAux.
    leftCur = left
    leftEnd = half
    rightCur = half + 1
    rightEnd = right
    auxCur = left

    # while none of the subarrays have reached an end.
    while leftCur <= leftEnd and rightCur <= rightEnd:
        if array[leftCur] <= array[rightCur]:
            arrayAux[auxCur] = array[leftCur]
            leftCur += 1
        else:
            arrayAux[auxCur] = array[rightCur]
            rightCur += 1
        auxCur += 1

    # only executes when the right subarray has reached an end and the left one hasn't.
    while leftCur <= leftEnd:
        arrayAux[auxCur] = array[leftCur]
        auxCur += 1
        leftCur += 1

    # only executes when the left subarray has reached an end and the right one hasn't.
    while rightCur <= rightEnd:
        arrayAux[auxCur] = array[rightCur]
        auxCur += 1
        rightCur += 1

    # now copy every element of the sorted arrayAux to the original array.
    for i in range(len(array)):
        array[i] = arrayAux[i]


##---------------------------------------##
#       MERGESORT - FINAL INSERTION       #
##---------------------------------------##
def mergeSortFI(array, left=0, right=-1, L=-1, arrayAux=None):
    # in the first execution, arrayAux will be none(null). arrayAux will be created and passed as
    # a parameter for the next executions.
    if right == -1:
        right = len(array) - 1
    if arrayAux is None:
        arrayAux = array[:]
    half = left + (right - left) // 2
    # checking whether the received array or subarray has more than one element.
    if left < right:
        if half - left > L:
            mergeSort(array, left, half, arrayAux)
        if right - half > L:
            mergeSort(array, half + 1, right, arrayAux)
        merge(array, left, right, half, arrayAux)
        insertionSort(array)

    return array


def merge(array, left, right, half, arrayAux):
    # cur variables will iterate through the array and make comparisons.
    # auxCur indicates the current position in arrayAux.
    leftCur = left
    leftEnd = half
    rightCur = half + 1
    rightEnd = right
    auxCur = left

    # while none of the subarrays have reached an end.
    while leftCur <= leftEnd and rightCur <= rightEnd:
        if array[leftCur] <= array[rightCur]:
            arrayAux[auxCur] = array[leftCur]
            leftCur += 1
        else:
            arrayAux[auxCur] = array[rightCur]
            rightCur += 1
        auxCur += 1

    # only executes when the right subarray has reached an end and the left one hasn't.
    while leftCur <= leftEnd:
        arrayAux[auxCur] = array[leftCur]
        auxCur += 1
        leftCur += 1

    # only executes when the left subarray has reached an end and the right one hasn't.
    while rightCur <= rightEnd:
        arrayAux[auxCur] = array[rightCur]
        auxCur += 1
        rightCur += 1

    # now copy every element of the sorted arrayAux to the original array.
    for i in range(len(array)):
        array[i] = arrayAux[i]


if __name__ == '__main__':
    array = [5, 1, 3, 7, 19, 8, 17, 3, 58, 33, 37, 9, 1, 7, 9]
    # array = [6, 1, 3, 4, 3, 2, 9, 3]
    #       [1, 2, 3, 3, 3, 4, 6, 9]
    # print(insertionSort(array))
    # print(selectionSort(array))
    # print(shellSort(array))
    # print(quickSort(array))  # quicksort
    # print(quickSortPI(array, L=10))  # quicksort with partial insertion
    # print(quickSortFI(array, L=5))  # quicksort with final insertion
    print(mergeSort(array))
    print(mergeSortPI(array, L=5))  # mergesort with final insertion
    print(mergeSortFI(array, L=2))  # mergesort with final insertion
