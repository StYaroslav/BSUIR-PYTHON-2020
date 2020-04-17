import unittest

from tasks.singleton import Singleton


class TestSingletonclass(unittest.TestCase):
    def test_singleton_metaclass(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertTrue(s1 == s2)