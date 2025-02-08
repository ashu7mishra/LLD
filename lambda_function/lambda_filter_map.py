from functools import reduce

mul = lambda x,y : x*y
print(mul(4, 5))

is_even = lambda x : x%2==0
print(is_even(4))

print(list(map(lambda x : x%2, [2, 3, 4])))

print(list(map(lambda x : x**2, [2, 3, 4])))

print(list(filter(lambda x : x%2==0, [2, 3, 4])))

l1 = [1,2,3,4,5]
print(reduce(lambda x,y: x+y, l1))

print(reduce(lambda x,y: x if x>y else y, l1))

words = ['hello', ' ', 'world']
print(reduce(lambda x,y: x+y, words))
