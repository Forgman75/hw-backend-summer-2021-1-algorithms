from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    import re
    if re.search(r'[a-zA-Zа-яА-Я]+', text):
        list_str = text.split()
        max_word = max(list_str, key=len)
        min_word = min(list_str, key=len)
    
        return (min_word, max_word)
    else:
        return (None, None)
