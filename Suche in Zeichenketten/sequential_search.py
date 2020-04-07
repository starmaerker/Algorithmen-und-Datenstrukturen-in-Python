import random

def sequential_search(list_to_search, item):
    position = 0
    found = False

    while position < len(list_to_search) and not found:
        if list_to_search[position] == item:
            found = True
        else:
            position += 1

    return found, position
