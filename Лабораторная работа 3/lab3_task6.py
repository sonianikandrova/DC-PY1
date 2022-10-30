list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maximum = 0
k = 0

for i in range(len(list_numbers)):
    if list_numbers[i]>maximum:
        maximum=list_numbers[i]
        k=i

list_numbers[k], list_numbers[-1] = list_numbers[-1], list_numbers[k]
print(list_numbers)
