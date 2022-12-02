from random import randint
def get_unique_list_numbers(min, max, size) -> list[int]:
    list_numbers = []
    while len (list_numbers)<size and size<=len(range(min, max))+1:
        s = randint(min, max)
        if s not in list_numbers:
            list_numbers.append(s)
    return list_numbers

min = int(-10)
max = int(10)
size = 15
list_unique_numbers = get_unique_list_numbers(min, max, size)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
