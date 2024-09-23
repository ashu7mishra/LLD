class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_unique_persons(people):
    # TODO: Implement the logic to find unique persons based on their names.
    # If there are multiple persons with the same name, only include the first
    # person encountered with that name in the returned list.


# Example usage:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 35)
person4 = Person("Charlie", 40)

people = [person1, person2, person3, person4]

unique_persons = find_unique_persons(people)
for person in unique_persons:
    print(f"Name: {person.name}, Age: {person.age}")
