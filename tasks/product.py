from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    new_list = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            new_list.append((arr1[i], arr2[j]))
            
    return new_list
