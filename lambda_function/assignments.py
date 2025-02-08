# Implement a function getDistinctNumbers that takes a list of numbers as input and returns a list
# containing only the distinct numbers from the input list.

from functools import reduce

def getDistinctNumbers(numbers):
    # code here
    return reduce(lambda x, y: x+[y] if y not in x else x, numbers, [])

print(getDistinctNumbers([1,2,3,2,2,2,3,3,4,4,5,1,2,5,6,7,7,7,8,8,8,9]))

def is_even(num):
    return num % 2 == 0


def double(num):
    return num * 2

# TODO: Implement the function below
def filter_and_double_even_numbers(numbers):
    # code here
    return list(map(lambda x: double(x),list(filter(lambda x: is_even(x), numbers))))

numbers = [1,2,3,4,5]
print(filter_and_double_even_numbers(numbers))

# You are given a list of strings having different fruit names. You need to filter out the names of the
# fruits whose name starts from the character A or a.

fruits = ['apple', 'orange']
def filter_fruits_starting_with_a(fruits):
    # Code here
    return list(filter(lambda x: x[0].upper()=='A', fruits))

print(filter_fruits_starting_with_a(fruits))

