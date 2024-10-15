months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    startdate = input('Date: ').strip()
    try:
        month,day,year = startdate.split(sep='/')
    except ValueError:
        try:
            month,day,year = startdate.split(sep=' ')
        except ValueError:
            pass
        else:
            if len(day) < 2:
                continue
            day = day[:-1]
            if not day.isdigit():
                continue
            day = int(day)
            if day > 31 or day < 1:
                continue
            year = int(year)
            month = month.title()
            if month in months:
                month = (months.index(month)) + 1
                if month > 12 or month < 1:
                    continue
                break
            else:
                pass
    else:
        day = int(day)
        if day > 31 or day < 1:
            continue
        if not month.isdigit():
            continue
        month = int(month)
        if month > 12 or month < 1:
            continue
        year = int(year)
        break

print(f'{year:04d}-{month:02d}-{day:02d}')
