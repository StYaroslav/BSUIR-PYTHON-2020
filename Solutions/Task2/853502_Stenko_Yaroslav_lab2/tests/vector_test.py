import unittest

from tasks.vector import Vector, DimensionError


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