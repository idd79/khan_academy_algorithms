# Implements the binary search algorithm

min = 0
max = 100_000
mylist1 = (min..max).to_a
mylist2 = min.step(max, 7).map { |i| i }
target = mylist1.sample

def binary_search(target, array)
  if array.empty?
    puts 'Target not present in the array'
    return -1
  end

  guess = array.size / 2
  value_guessed = array[guess]

  return value_guessed if value_guessed == target

  new_array = value_guessed < target ? array[guess + 1..-1] : array[0...guess]

  binary_search(target, new_array)
end

p target
p binary_search(target, mylist1)
p binary_search(target, mylist2)
