def cached(func):
    temp_dict = {}

    def wrapper(*args, **kwargs):
        if args in temp_dict:
            return temp_dict[args]
        else:
            try:
                return_value = func(*args, **kwargs)
            except Exception:
                return
            temp_dict[args] = return_value
            return return_value

    return wrapper


@cached
def diff_function(a, b):
    return a - b