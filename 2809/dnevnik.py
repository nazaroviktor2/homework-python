"""Create file captain's diary."""
import datetime


def dnevnik(day: int, month: int, year: int, notes: list) -> None:
    """Keeps a captain's diary and creates file with dated notes.

    Args:
        day: int some day
        month: int some month
        year: int some year
        notes: list - captain's notes
    """
    start_date = datetime.date(year, month, day)
    finish_date = start_date + datetime.timedelta(len(notes))
    with open("записи за {0}-{1}.txt".format(start_date, finish_date), "w") as file_name:
        for index, note in enumerate(notes):
            file_name.write("{0}: {1}\n".format(start_date + datetime.timedelta(index), note))
