import argparse
from tasks_examples.examples import external_sort_example, to_json_example, vector_example, from_json_example, \
    cached_decorator_example, singleton_example

tasks = {1: external_sort_example,
         2: to_json_example,
         3: vector_example,
         4: cached_decorator_example,
         5: from_json_example,
         6: singleton_example}


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_number', choices=[1, 2, 3, 4, 5, 6], type=int, help='Tasks numbers: 1 - external merge '
                                                                                  'sort\n 2 - to json converter \n 3 '
                                                                                  '- vector \n 4 - cached decorator '
                                                                                  '\n 5 - from json converter \n 6 - '
                                                                                  'singleton')
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    if namespace.task_number == 1:
        tasks[1]()
    elif namespace.task_number == 2:
        tasks[2]()
    elif namespace.task_number == 3:
        tasks[3]()
    elif namespace.task_number == 4:
        tasks[4]()
    elif namespace.task_number == 5:
        tasks[5]()
    elif namespace.task_number == 6:
        tasks[6]()


if __name__ == "__main__":
    main()
