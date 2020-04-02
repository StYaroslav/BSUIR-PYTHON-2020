import re

try:
    from json_serializer import to_json, Person
except ModuleNotFoundError:
    from .json_serializer import to_json, Person


def from_json(json):
    edited_string = re.findall(r'\w+|[{\[\]]', json)
    edited_string_iterator = iter(edited_string)
    return converter(edited_string_iterator)


def converter(edited_string_iterator):
    next_value = next(edited_string_iterator)
    if next_value == "{":
        result_dict = {}
        while True:
            try:
                key = converter(edited_string_iterator)
                result_dict[key] = converter(edited_string_iterator)
            except StopIteration:
                return result_dict
    elif next_value == "[":
        result_list = []
        while True:
            next_list_value = converter(edited_string_iterator)
            if next_list_value == ']':
                return result_list
            else:
                result_list.append(next_list_value)
    elif next_value.isdigit():
        return int(next_value)
    elif next_value == 'null':
        return None
    elif next_value == 'true':
        return True
    elif next_value == 'false':
        return False
    else:
        return next_value