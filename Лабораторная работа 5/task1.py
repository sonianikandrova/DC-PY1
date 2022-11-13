# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list =[]
for i in range (16):
    dict = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    list.append(dict)

pprint(list)
