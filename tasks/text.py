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
        arr_lens = list(map(len, list_str))
        maxim_len = max(arr_lens)
        minim_len = min(arr_lens)
        for word in list_str:
            if len(word) == maxim_len:
                max_word = word
            elif len(word) == minim_len:
                min_word = word
        return (min_word, max_word)
    else:
        return (None, None)
