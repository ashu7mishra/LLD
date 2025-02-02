# age: int = 10
# print(age)
# # age = "I don't know"
# age = 10.00
# print(age)


# typing techniques

x: float = 0
def squareDivideBy2(num: float) -> float:
    return num*num/2

x = squareDivideBy2(5)
print(x)

def square(num: float) -> None:
    print(num*num)

square(5)

from typing import List, Dict
numbers: List[int] = [1,2,3]
# numbers: list[int] = [1,2,3]

# numDict: dict[int, str] = {1:'abc', 2:'def', 3: 'ghi'}
numDict: Dict[int, str] = {1:'abc', 2:'def', 3: 'ghi'}
print(numDict)

numSet: set[str] = {'abc', 'def', 'ghi'}
print(numSet)

# ll: list[list[int]] = [[1,2,3],[4,5,'dfvkbfv']] #error
ll: list[list[int]] = [[1,2,3],[4,5,6]]
print(ll)

vector = list[list[int]]

# ll2: vector = [[1,2,3,4], [5,6,7,8]]
ll2: vector = [[1,2,3,4], ['sofvn',6,7,8]] #error
print(ll2)