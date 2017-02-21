# Swap between two elements in an array

def swap(array, firstIndex, secondIndex)
  array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]

  array
end

testArray = [7, 9, 4]
p swap(testArray, 1, 2)

# Takes an array and a number startIndex, and returns the index of the smallest
# value that occurs with index startIndex or greater. If this smallest value
# occurs more than once in this range, then return the index of the leftmost
# occurrence within this range.

def indexOfMinimum(array, startIndex)
  min_index = startIndex

  (startIndex + 1).upto(array.size - 1) do |i|
    min_index = i if array[min_index] > array[i]
  end

  min_index
end

p indexOfMinimum([5, 4, 10, 9], 2)
p indexOfMinimum([5, 4, 10, 9], 0)

# Implement selection sort

def selectionSort(array)
  0.upto(array.length - 2) do |i|
    index_min = indexOfMinimum(array, i)
    swap(array, i, index_min)
  end

  array
end

p selectionSort([7, 4, 3, 3, 1])
p selectionSort(['Yusuf', 'Ivan'])
