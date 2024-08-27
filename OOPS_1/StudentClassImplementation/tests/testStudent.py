import unittest

from config.student import Student


class TestStudent(unittest.TestCase):
    def test_init(self):
        person = Student("Alice", 25)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 25)

if __name__ == "__main__":
    unittest.main()