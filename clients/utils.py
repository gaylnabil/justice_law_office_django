
def get_key_dict(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key
    return 0
