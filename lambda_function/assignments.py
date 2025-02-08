# Implement a function getDistinctNumbers that takes a list of numbers as input and returns a list
# containing only the distinct numbers from the input list.

from functools import reduce

def getDistinctNumbers(numbers):
    # code here
    return reduce(lambda x, y: x+[y] if y not in x else x, numbers, [])

print(getDistinctNumbers([1,2,3,2,2,2,3,3,4,4,5,1,2,5,6,7,7,7,8,8,8,9]))



# Implement a function filter_and_double_even_numbers that takes a list of integers as input.
# It should filter out the even numbers from the input list, double each of them, and return a
# list containing the doubled values.
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


# Given a list of strings sentences representing sentences, write a Python method called processSentences
# that performs the following operations:
#
# Filter out sentences that contain the word "python".
# Map each filtered sentences to its length.
# Find the average length of the sentences.
# Convert the average length to an integer by rounding down.
# Return the rounded average length.

# TODO: Complete the given function
from functools import reduce
def processSentences(sentences):
    # Code here
    # Filter out sentences containing the word "python"
    filtered_sentences = list(filter(lambda x: "python" in x, sentences))

    # Map each remaining sentence to its length
    sentence_lengths = list(map(lambda x: len(x),filtered_sentences))
    # sentence_lengths = list(map(lambda x: len(x),list(filter(lambda x: "python" in x, sentences))))

    # Find the average length of the sentences
    if sentence_lengths:
        average_length = reduce(lambda x,y: x+y,sentence_lengths,0) / len(sentence_lengths)
    else:
        average_length = 0

    # Convert the average length to an integer by rounding down
    rounded_average_length = int(average_length)

    return rounded_average_length

sentences = ["I've python", "aIYDCisbdv", "sdvspythonsjdbc"]

print(processSentences(sentences))

