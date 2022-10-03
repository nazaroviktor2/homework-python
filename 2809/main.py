"""Main for dnevnik."""
from dnevnik import dnevnik

if __name__ == '__main__':
    notes = ['завтра 20 января 2033 года, меня наконец то отчислят.',
             'меня снова не отчислили.',
             'новый день, до попытки отчисления осталось 364 дня.'
             ]
    date = "19.01.2033"
    day, month, year = map(int, date.split("."))
    dnevnik(day, month, year, notes)
