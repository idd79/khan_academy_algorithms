# Implements the binary search algorithm
# Returns the position of the element found, otherwise returns -1

min = 0
max = 1_000_000
mylist1 = (min..max).to_a
mylist2 = min.step(max, 3).map { |i| i }
target = mylist1.sample

def binary_search(target, array, min, max)
  return -1 if min > max

  guess = min + (max - min) / 2
  value_guessed = array[guess]

  return guess if value_guessed == target
  return binary_search(target, array, guess + 1, max) if value_guessed < target
  binary_search(target, array, min, guess - 1)
end

# Recursive algorithm with only two inputs: array and target
def binary_search3(target, array)
  min = 0
  max = array.size - 1

  recursive_search = lambda do |x, list, lb, ub|
    return -1 if lb > ub

    guess = lb + (ub - lb) / 2
    value_guessed = list[guess]

    return guess if value_guessed == x
    return recursive_search.call(x, list, guess + 1, ub) if value_guessed < x
    recursive_search.call(x, list, lb, guess - 1)
  end

  recursive_search.call(target, array, min, max)
end

p target
p binary_search(target, mylist1, 0, mylist1.size - 1)
p binary_search(target, mylist2, 0, mylist2.size - 1)
p binary_search3(target, mylist1)
p binary_search3(target, mylist2)

# Non-recursive algorithm:

def binary_search2(target, array)
  min = 0
  max = array.size - 1

  while min <= max
    guess = min + (max - min) / 2
    value_guessed = array[guess]

    return guess if value_guessed == target

    value_guessed < target ? min = guess + 1 : max = guess - 1
  end

  -1
end

# p binary_search2(10, [2, 3, 4, 10, 40])
p binary_search2(target, mylist1)
p binary_search2(target, mylist2)
