class Person:
    class SelfInfo:

        def __init__(self, first_name, last_name, ref):
            self.first_name = first_name
            self.last_name = last_name
            self.ref = ref

    def __init__(self, country, age, is_adult, mail=None):
        self.country = country
        self.age = age
        self.adult = is_adult
        self.mail = mail
        self.info = Person.SelfInfo('oleg', 'pipeg', [1, 3, 4])


def to_json(obj):
    result = ''
    if isinstance(obj, int):
        if obj is True:
            return 'true'
        elif obj is False:
            return 'false'
        else:
            return str(obj)
    elif obj is None:
        return 'null'
    elif isinstance(obj, str):
        return '"{}"'.format(obj)
    elif isinstance(obj, list):
        result += '['
        for element in obj:
            result += to_json(element)
            result += ', '
        result = result[0:-2]
        result += ']'
        return result
    elif isinstance(obj, tuple):
        result += '('
        for element in obj:
            result += to_json(element)
            result += ', '
        result = result[0:-2]
        result += ')'
        return result
    elif isinstance(obj, dict):
        result += '{'
        for key, value in obj.items():
            result += to_json(key)
            result += ': '
            result += to_json(value)
            result += ', '
        result = result[0:-2]
        result += '}'
        return result
    else:
        return to_json(obj.__dict__)