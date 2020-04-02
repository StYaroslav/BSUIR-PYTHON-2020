import sys
import tempfile


class HeapNode:

    def __init__(self, item, file_handler):
        self.item = item
        self.file_handler = file_handler


def heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i].item > array[left].item:
        smallest = left
    if right <= length and array[smallest].item > array[right].item:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, smallest)


def construct_min_heap(array):
    for i in reversed(range(len(array) // 2)):
        heapify(array, i)


def split_file(init_file, small_file_size):
    temp_files = []
    with open(init_file) as file:
        temp_buffer = []
        size = 0
        while True:
            number = file.readline()
            if not number:
                break
            temp_buffer.append(int(number))
            size += 1
            if size % small_file_size == 0:
                temp_buffer.sort()
                temp_file = tempfile.NamedTemporaryFile(mode='w+t')
                for item in temp_buffer:
                    temp_file.writelines("{}\n".format(str(item)))
                temp_file.seek(0)
                temp_files.append(temp_file)
                temp_buffer.clear()
    return temp_files


def merge_split_files(temp_files):
    min_elements_list = []
    for file in temp_files:
        item = int(file.readline().strip())
        min_elements_list.append(HeapNode(item, file))
    construct_min_heap(min_elements_list)
    with open('sorted_file.txt', 'w') as sorted_file:
        while True:
            min = min_elements_list[0]
            if min.item == sys.maxsize:
                break
            sorted_file.writelines("{}\n".format(str(min.item)))
            file_handler = min.file_handler
            item = file_handler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            min_elements_list[0] = HeapNode(item, file_handler)
            heapify(min_elements_list, 0)
    for file in temp_files:
        file.close()
