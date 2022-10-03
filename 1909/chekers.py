def check_date(year: int, month: int, day: int) -> bool:
    """Takes year, month, day and checks does the date exist.

    Args:
        year : int - some year.
        month : int - some month.
        day : int - some day.

    Returns:
        bool :  true if the date exist else false.
    """
    if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:
        return True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        return True
    elif month == 2:
        if abs(year) % 100 == 0 and abs(year) % 400 == 0 or \
                abs(year) % 4 == 0 and abs(year) % 100 != 0:
            if 0 < day <= 29:
                return True
        elif 0 < day <= 28:
            return True
    return False
