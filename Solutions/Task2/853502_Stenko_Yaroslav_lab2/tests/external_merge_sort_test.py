import random
import os
import time
import unittest

from tasks.external_merge_sort import split_file, merge_split_files


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
        self.start_time = time.time()
        self.input_check = [0] * 1
        with open('numbers.txt', 'w') as self.file:
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))

    def test_file_is_sorted(self):
        temp_files_list = split_file(os.getcwd() + "\\numbers.txt", 100000, self.input_check)
        merge_split_files(temp_files_list, self.input_check)
        duration = time.time() - self.start_time
        print("Big file performance duration: ", duration)
        self.assertTrue(file_is_sorted())


class TestExternalSortPerfomanceSmallFile(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.input_check = [0] * 1
        with open('numbers.txt', 'w') as self.file:
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(100000))

    def test_perfomance(self):
        temp_files_list = split_file(os.getcwd() + "\\numbers.txt", 100000, self.input_check)
        merge_split_files(temp_files_list, self.input_check)

    def tearDown(self):
        duration = time.time() - self.start_time
        print("Small file performance duration: ", duration)


class TestExternalSortErrorOccurrence(unittest.TestCase):
    def setUp(self):
        self.input_check = [0] * 1
        with open('numbers.txt', 'w') as self.file:
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000))
            self.file.write('smthng\n')
            self.file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000))

    def test_external_sort_value_error(self):
        self.assertRaises(Exception, split_file, 'numbers.txt', self.input_check, 1000)
