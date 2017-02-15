# Implements the binary search algorithm
# Returns the position of the element found, otherwise returns -1

import random as rnd
# from IPython import embed

min = 0
max = 1_000_000
mylist1 = list(range(min, max))
mylist2 = list(range(min, max, 3))
target = rnd.sample(mylist1, 1)[0]


# Recursive algorithms

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


def binary_search3(target, array):
    min = 0
    max = len(array) - 1

    def recursive_search(x, list, lb, ub):
        if lb > ub:
            return -1

        else:
            guess = lb + (ub - lb) // 2
            value_guessed = array[guess]

            if value_guessed == target:
                return guess
            elif value_guessed < target:
                return recursive_search(target, array, guess+1, ub)
            else:
                return recursive_search(target, array, lb, guess-1)

    return recursive_search(target, array, min, max)

print(target)
print(binary_search(target, mylist1, 0, len(mylist1)-1))
print(binary_search(target, mylist2, 0, len(mylist2)-1))
print(binary_search3(target, mylist1))
print(binary_search3(target, mylist2))


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
