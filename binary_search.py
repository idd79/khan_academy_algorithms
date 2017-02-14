# Implements the binary search algorithm
# Returns the position of the element found, otherwise returns -1

import random as rnd
# from IPython import embed

min = 0
max = 1000000
mylist1 = list(range(min, max))
mylist2 = list(range(min, max, 3))
target = rnd.sample(mylist1, 1)[0]


def binary_search(target, array, min, max):
    if min > max:
        return -1

    else:
        guess = min + (max - min) // 2
        value_guessed = array[guess]

        if value_guessed == target:
            return guess
        elif value_guessed < target:
            return binary_search(target, array, guess+1, max)
        else:
            return binary_search(target, array, min, guess-1)

print(target)
print(binary_search(target, mylist1, 0, len(mylist1)-1))
print(binary_search(target, mylist2, 0, len(mylist2)-1))

# Non-recursive algorithm:


def binary_search2(target, array):
    min = 0
    max = len(array) - 1

    while min <= max:
        guess = min + (max - min) // 2
        value_guessed = array[guess]

        if value_guessed == target:
            return guess
        elif value_guessed < target:
            min = guess + 1
        else:
            max = guess - 1

    return -1

print(binary_search2(target, mylist1))
print(binary_search2(target, mylist2))
