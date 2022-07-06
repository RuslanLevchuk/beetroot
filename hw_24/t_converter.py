"""
Приклад використання доктесту. Для того, щоб запустити доктест, в терміналі потрібно за допомогогою python3 (py для windows)
запустити даний скрипт та додати ключ -v:
python3 t_converter.py -v

У даному випадку перевіряємо, чи працює конвертація 30С фаренгейти (86F)

>>> converter('30C')
(86, 'F', '86F')

Також перевіримо, чи виникне помилка

>>> converter('30')
Traceback (most recent call last):
    ...
ValueError: Input proper convention

переведемо з фаренгейта у сельсія
>>> converter('68F')
(20, 'C', '20C')
"""

def converter(T):
    """to convert temerature string value must contain integer and temperature symbol:
    '32F' or '18C'
    function returns tuple which contains three elements:
    integer-type result (for example 12),
    string-type symbol ('F' or 'C')
    and full string-type result (for example '12F'):
    (12, 'C', '12C')
    """
    measure = T[-1]
    degree = int(T[:-1])
    if measure.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        out_measure = "F"
    elif measure.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        out_measure = "C"
    else:
        raise ValueError("Input proper convention")
    return result, out_measure, f'{result}{out_measure}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()