# Implement a function getDistinctNumbers that takes a list of numbers as input and returns a list
# containing only the distinct numbers from the input list.

from functools import reduce

def getDistinctNumbers(numbers):
    # code here
    return reduce(lambda x, y: x+[y] if y not in x else x, numbers, [])

print(getDistinctNumbers([1,2,3,2,2,2,3,3,4,4,5,1,2,5,6,7,7,7,8,8,8,9]))

