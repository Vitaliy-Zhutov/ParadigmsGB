# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру 
# для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


from random import randint
from typing import List


def sorted_numbers(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError('A non-empty integer list must be submitted to the input')
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [randint(0, 100) for i in range(10)]
print(numbers)

sorted_numbers = sorted(numbers, reverse = True)
print(sorted_numbers)
