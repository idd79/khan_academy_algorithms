# Swap between two elements in an array
# from IPython import embed


def swap(array, firstIndex, secondIndex):
    array[firstIndex], array[secondIndex] = array[secondIndex], \
        array[firstIndex]
    return array

testArray = [7, 9, 4]
print(swap(testArray, 1, 2))

# Takes an array and a number startIndex, and returns the index of the smallest
# value that occurs with index startIndex or greater. If this smallest value
# occurs more than once in this range, then return the index of the leftmost
# occurrence within this range.


def indexOfMinimum(array, startIndex):
    min_index = startIndex
    for i in range(startIndex + 1, len(array)):
        if array[min_index] > array[i]:
            min_index = i

    return min_index


print(indexOfMinimum([5, 4, 10, 9], 2))

# Implement selection sort


def selectionSort(array):
    for i in range(0, len(array) - 1):
        index_min = indexOfMinimum(array, i)
        swap(array, i, index_min)

    return array


print(selectionSort([7, 4, 3, 3, 1]))
print(selectionSort(['Yusuf', 'Ivan']))
