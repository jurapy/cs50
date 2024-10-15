from datetime import date

import sys
import datetime
import inflect


def main():
    born = get_date(get_input())
    today = datetime.date.today()
    difference_minutes = get_minutes(born, today)
    p = inflect.engine()
    print(p.number_to_words(difference_minutes, andword='').capitalize() + ' minutes')


def get_input():
    date = input('Date of Birth: ')
    return date

def get_date(start_date):
    try:
        year,month,day = start_date.split(sep='-')
        year,month,day = tuple(map(int, (year,month,day)))
        complete_date = datetime.date(year, month, day)
    except Exception:
        sys.exit('Invalid date')
    else:
        return complete_date


def get_minutes(born, today):
    difference = today - born
    return difference.days * 1440


if __name__ == "__main__":
    main()
