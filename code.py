from itertools import count, compress

def odd_numbers():
    for i in count(1):
        if i % 2 == 1:
            yield i

def even_numbers():
    for i in count(2):
        if i % 2 == 0:
            yield i

numbers = compress(list(odd_numbers()) + list(even_numbers()), [True] * 10)

for number in numbers:
    print(number)
