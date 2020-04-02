import random
from tasks.external_merge_sort import split_file, merge_split_files
from tasks.json_serializer import Person, to_json
from tasks.vector import Vector
from tasks.cached import diff_function
from tasks.json_deserializer import from_json
from tasks.singleton import Singleton


def external_sort_example():
    total_numbers_in_file = 1000000
    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(total_numbers_in_file))
    small_file_size = total_numbers_in_file / 10
    temp_files_list = split_file('numbers.txt', small_file_size)
    merge_split_files(temp_files_list)


def to_json_example():
    person = Person('belarus', 18, True)
    print("Python object: ", person.__dict__)
    json_string = to_json(person)
    print("Json string: ", json_string)


def vector_example():
    v1 = Vector(1, 3, 4)
    v2 = Vector(2, 5, 6)
    print("Vector representation: ", v1)
    print("Multiplication with constant number 3: ", v1 * 3)
    print("Multiplication of 2 vectors: ")
    print("First vector: ", v1)
    print("Second vector: ", v2)
    print("Multiplication result: ", v1 * v2)
    print("Sum result(same vectors): ", v1 + v2)
    print("Length of first vector: ", len(v1))
    print("Checking for equality: ", v1 == v2)
    print("Subtraction of two vectors: ", v1 - v2)
    print("Result of taking value by index from first vector: \nv1[2] = ", v1[2])


def cached_decorator_example():
    print("Input params 3 and 5 \n Result:  ", diff_function(3, 5))
    print("Again input same params 3 and 5 \n Result: ", diff_function(3, 5))
    print("Input params 2 and 8 \n Result: ", diff_function(2, 8))


def from_json_example():
    person = Person('belarus', 18, True)
    json_string = to_json(person)
    print("Json string: ", json_string)
    python_object = from_json(json_string)
    print("Python object: ", python_object)


def singleton_example():
    print("Creating first instance s1 = Singleton():")
    s = Singleton()
    print(s)
    print("Creating second instance s2 = Singleton():")
    s1 = Singleton()
    print(s1)
