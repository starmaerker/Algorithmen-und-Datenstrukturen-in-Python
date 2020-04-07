import random


def sequential_search(list_to_search, item):
    position = 0
    found = False

    while position < len(list_to_search) and not found:
        if list_to_search[position] == item:
            found = True
        else:
            position += 1

    return found, item, position


list_to_search = []
item = random.randint(0, 100)

for _ in range(100):
    list_to_search.append(random.randint(0, 100))

print(sequential_search(list_to_search, item))
