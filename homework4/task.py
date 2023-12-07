"""
Задача. Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму.
"""

def pearson_correlation(array1, array2):

     # Проверка на то, что массивы одинаковой длины
    if len(array1) != len(array2):
        raise ValueError("Массивы должны быть одинаковой длины")

    # Рассчитаем средние значения
    mean_x = sum(array1) / len(array1)
    mean_y = sum(array2) / len(array2)

    # Рассчитаем квадратные отклонения
    variance_x = sum((xi - mean_x) ** 2 for xi in array1)
    variance_y = sum((yi - mean_y) ** 2 for yi in array2)

    # Рассчитаем корреляцию
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(array1, array2))
    correlation = numerator / ((variance_x ** 0.5) * (variance_y ** 0.5))

    return correlation


# Пример использования
array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10]
pearcor = pearson_correlation(array1, array2)
print(f'Корреляция Пирсона = {pearcor}')  