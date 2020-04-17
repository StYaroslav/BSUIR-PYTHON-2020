import re

try:
    from json_serializer import to_json, Person
except ModuleNotFoundError:
    from tasks.json_serializer import to_json, Person


class FormatException(Exception):
    print("Input string doesn't match json string parameters!")


def from_json(json):
    invalid_key_pattern = re.compile('[^"]:')
    invalid_bool_pattern = re.compile('(True|False)')
    invalid_null_pattern = re.compile('None')
    try:
        if re.search(invalid_key_pattern, json) or re.search(invalid_bool_pattern, json) or re.search(invalid_null_pattern, json):
            raise FormatException
    except SyntaxError:
        raise FormatException
    edited_string = re.findall(r'\w+|["{\[\]]', json)
    edited_string_iterator = iter(edited_string)
    return converter(edited_string_iterator)


def converter(edited_string_iterator):
    next_value = next(edited_string_iterator)
    if next_value == "{":
        result_dict = {}
        while True:
            try:
                key = next(edited_string_iterator)
                if key == '"':
                    key = next(edited_string_iterator)
                    next(edited_string_iterator)
                    result_dict[key] = converter(edited_string_iterator)
            except StopIteration:
                return result_dict
    elif next_value == "[":
        result_list = []
        while True:
            next_list_value = converter(edited_string_iterator)
            if next_list_value == '"':
                next_list_value = next(edited_string_iterator)
                next(edited_string_iterator)
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
