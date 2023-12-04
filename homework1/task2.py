# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру 
# для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки. 

from random import randint
from typing import List


def sorted_numbers(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError('A non-empty integer list must be submitted to the input')
    return sorted(arr, reverse = True)


numbers = [randint(0, 100) for i in range(10)]
print(numbers)
print(sorted_numbers(numbers))
