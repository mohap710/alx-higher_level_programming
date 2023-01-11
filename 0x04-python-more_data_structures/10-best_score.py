#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    max = 0
    max_key = None
    for (key, value) in a_dictionary.items():
        if value > max:
            max = value
            max_key = key
    return max_key
