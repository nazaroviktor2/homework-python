"""Main for chekers."""
from chekers import check_date

if __name__ == '__main__':

    try:
        year = int(input("Введите год - "))
        month = int(input("Введите месяц (числом) - "))
        day = int(input("Введите день - "))

    except ValueError:
        print('Неверный формат ввода')

    else:
        if check_date(year, month, day):

            print('Дата {0}.{1}.{2} - существует'.format(day, month, year))

        else:
            print('Дата {0}.{1}.{2} - не существует'.format(day, month, year))
