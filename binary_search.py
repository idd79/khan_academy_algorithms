# Implements the binary search algorithm

import random as rnd

min = 0
max = 100000
mylist1 = list(range(min, max))
mylist2 = list(range(min, max, 3))
target = rnd.sample(mylist1, 1)[0]


def binary_search(target, array):
    if len(array) == 0:
        print('Target not present in the array')
        return -1
 
    guess = len(array) // 2
    value_guessed = array[guess]
 
    if value_guessed == target: return value_guessed
    
    new_array = array[guess + 1:] if value_guessed < target else array[0:guess]
 
    return binary_search(target, new_array)


print(target)
print(binary_search(target, mylist1))
print(binary_search(target, mylist2))
