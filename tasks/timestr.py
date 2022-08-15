__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    days_str = f'{days:02d}d'
    hrs_str = f'{hours:02d}h'
    mins_str = f'{minutes:02d}m'
    sec_str = f'{sec:02d}s'

    if days:
        return f'{days_str}{hrs_str}{mins_str}{sec_str}'

    if hours:
        return f'{hrs_str}{mins_str}{sec_str}'

    if minutes:
        return f'{mins_str}{sec_str}'

    return sec_str

  





