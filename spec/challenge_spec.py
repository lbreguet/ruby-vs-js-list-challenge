import os
import sys
import unittest

print('Python version:', sys.version)

current_working_directory = os.getcwd()
lib_directory = current_working_directory + '/lib'
sys.path.append(lib_directory)

from challenge import challenge_any, challenge_none, challenge_one, challenge_all


def is_even(n): return n % 2 == 0
def is_one(n): return n == 1
def is_less_than_ten(n): return n < 10
def is_greater_than_ten(n): return n > 10


predicates = [is_even, is_one, is_less_than_ten, is_greater_than_ten]
array = [x for x in range(0, 10)]


class AnyTest(unittest.TestCase):
    def test_empty_array(self):
        for predicate in predicates:
            self.assertFalse(challenge_any([], predicate))

    def test_no_elements_match(self):
        self.assertFalse(challenge_any(array, is_greater_than_ten))

    def test_more_than_one_element_matches(self):
        self.assertTrue(challenge_any(array, is_even))

    def test_all_elements_match(self):
        self.assertTrue(challenge_any(array, is_less_than_ten))


class NoneTest(unittest.TestCase):
    def test_empty_array(self):
        for predicate in predicates:
            self.assertTrue(challenge_none([], predicate))

    def test_no_elements_match(self):
        self.assertTrue(challenge_none(array, is_greater_than_ten))

    def test_more_than_one_element_matches(self):
        self.assertFalse(challenge_none(array, is_even))

    def test_all_elements_match(self):
        self.assertFalse(challenge_none(array, is_less_than_ten))


class OneTest(unittest.TestCase):
    def test_empty_array(self):
        for predicate in predicates:
            self.assertFalse(challenge_one([], predicate))

    def test_no_elements_match(self):
        self.assertFalse(challenge_one(array, is_greater_than_ten))

    def test_exactly_one_element_matches(self):
        self.assertTrue(challenge_one(array, is_one))

    def test_more_than_one_element_matches(self):
        self.assertFalse(challenge_one(array, is_even))

    def test_all_elements_match(self):
        self.assertFalse(challenge_one(array, is_less_than_ten))


class AllTest(unittest.TestCase):
    def test_empty_array(self):
        for predicate in predicates:
            self.assertTrue(challenge_all([], predicate))

    def test_no_elements_match(self):
        self.assertFalse(challenge_all(array, is_greater_than_ten))

    def test_more_than_one_element_matches(self):
        self.assertFalse(challenge_all(array, is_even))

    def test_all_elements_match(self):
        self.assertTrue(challenge_all(array, is_less_than_ten))


if __name__ == '__main__':
    unittest.main()
