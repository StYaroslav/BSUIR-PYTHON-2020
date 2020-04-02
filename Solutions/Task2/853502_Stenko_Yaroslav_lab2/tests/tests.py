import unittest
from tasks.vector import Vector, DimensionError
from tasks.json_serializer import to_json, Person
import json
import random
import os
from tasks.external_merge_sort import merge_split_files, split_file
from tasks.json_deserializer import from_json
from tasks.singleton import Singleton
from tasks.cached import cached
import coverage


class TestVector(unittest.TestCase):
    def setUp(self):
        self.first_vector = Vector(1, 3, 5, 6)
        self.second_vector = Vector(2, 5, 8, 1)

    def test_vector_add(self):
        expected_array = [3, 8, 13, 7]
        self.assertTrue(expected_array, self.first_vector + self.second_vector)

    def test_vector_mul(self):
        expected_result = 63
        self.assertTrue(expected_result, self.second_vector * self.first_vector)

    def test_vector_mul_with_const_number(self):
        expected_array = [3, 9, 15, 18]
        self.assertTrue(expected_array, self.first_vector * 3)

    def test_vector_sub(self):
        expected_array = [1, 2, 3, -5]
        self.assertTrue(expected_array, self.second_vector - self.first_vector)

    def test_vector_len(self):
        expected_result = 4
        self.assertTrue(expected_result, len(self.first_vector))

    def test_vector_eq(self):
        self.assertFalse(self.first_vector == self.second_vector)
        test_vector = [2, 5, 8, 1]
        self.assertTrue(self.second_vector == test_vector)

    def test_vector_repr(self):
        expected_result = '[1, 3, 5, 6]'
        self.assertTrue(expected_result, self.first_vector)

    def test_vector_idexing(self):
        expected_result = 3
        self.assertTrue(expected_result, self.first_vector[1])

    def test_vector_dimension_error(self):
        test_vector = [1, 5, 6, 7, 8, 53]
        self.assertRaises(DimensionError, lambda: self.first_vector * test_vector)

    def test_vector_type_error(self):
        self.assertRaises(TypeError, lambda: self.first_vector + 5)


class TestToJsonConverter(unittest.TestCase):
    def setUp(self):
        self.person = Person('belarus', 18, True)
        self.expected_string = '{"country": "belarus", "age": 18, "adult": true, "mail": null, "info": {"first_name": "oleg", "last_name": "pipeg", "ref": [1, 3, 4]}}'

    def test_normal_performance(self):
        self.assertEqual(self.expected_string, to_json(self.person))

    def test_to_json_validation(self):
        json_string = to_json(self.person)

        def is_valid_json(json_string):
            try:
                json.loads(json_string)
            except ValueError:
                return False
            return True

        self.assertTrue(is_valid_json(json_string))


def file_is_sorted():
    with open('sorted_file.txt', 'r') as sorted_file:
        first_value = sorted_file.readline()
        second_value = sorted_file.readline()
        while True:
            if second_value:
                if int(first_value) > int(second_value):
                    return False
                first_value = second_value
                second_value = sorted_file.readline()
            else:
                break
        return True


class TestExternalSortResult(unittest.TestCase):
    def setUp(self):
        with open('numbers.txt', 'w') as self.file:
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))

    def test_file_is_sorted(self):
        temp_files_list = split_file(os.getcwd() + "\\numbers.txt", 100000)
        merge_split_files(temp_files_list)
        self.assertTrue(file_is_sorted())


class TestExternalSortErrorOccurrence(unittest.TestCase):
    def setUp(self):
        with open('numbers.txt', 'w') as self.file:
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000))
            self.file.write('smthng\n')
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000))

    def test_external_sort_value_error(self):
        self.assertRaises(ValueError, split_file, 'numbers.txt', 1000)


class TestFromJson(unittest.TestCase):
    def setUp(self):
        self.json_string = '{"country": "belarus", "age": 18, "adult": true, "mail": null, "info": {"first_name": "oleg", "last_name": "pipeg", "ref": [1, 3, 4]}}'

    def test_from_json_converter(self):
        expected_object = {'country': 'belarus', 'age': 18, 'adult': True, 'mail': None,
                           'info': {'first_name': 'oleg', 'last_name': 'pipeg', 'ref': [1, 3, 4]}}
        self.assertEqual(expected_object, from_json(self.json_string))

    def test_from_json_validation(self):
        def is_valid_from_json():
            try:
                json.dumps(from_json(self.json_string))
            except ValueError:
                return False
            return True

        self.assertTrue(is_valid_from_json())


class TestCachedDecorator(unittest.TestCase):
    @cached
    def mul_func(self, a, b):
        return a * b

    def test_cached_decorator(self):
        self.assertTrue(5 == self.mul_func(5, 1))
        self.mul_func(5, 1)
        self.assertTrue(5 == self.mul_func(5, 1))
        self.assertFalse(5 == self.mul_func(2, 6))

    def test_cached_error(self):
        self.assertRaises(Exception, self.mul_func('123', 4))


class TestSingletonclass(unittest.TestCase):
    def test_singleton_metaclass(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertTrue(s1 == s2)