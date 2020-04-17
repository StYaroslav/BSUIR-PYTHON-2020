import unittest

from tasks.cached import cached


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