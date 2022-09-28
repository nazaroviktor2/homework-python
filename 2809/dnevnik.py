import calendar
import datetime


def dnevnik(date, notes):
    day, month, year = map(int, date.split("."))
    start_date = datetime.date(year, month, day)
    finish_date = start_date + datetime.timedelta(len(notes))
    calendar.Calendar().itermonthdays()
    file = open(f"записи за {start_date}-{finish_date}.txt", "w")
    for i, note in enumerate(notes):
        file.write(f"{start_date + datetime.timedelta(i)}: {note}\n")

    file.close()
