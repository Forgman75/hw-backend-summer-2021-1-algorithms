__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_numbs = []
    odd_numbs = []
    for number in arr:
        if number % 2 == 0:
            even_numbs.append(number)
        else:
            odd_numbs.append(number)
    
    sum_even = sum(even_numbs)
    sum_odd = sum(odd_numbs)
    if sum_odd != 0:
        ratio = sum_even/sum_odd
        return round(ratio, 4)
    else:
        return 0

