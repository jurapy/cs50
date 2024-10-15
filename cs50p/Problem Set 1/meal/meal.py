def main():
    strtime = input('time: ')
    newtime = convert(strtime)

    if newtime >= 7 and newtime <= 8:
        print('breakfast time')
    elif newtime >= 12 and newtime <= 13:
        print('lunch time')
    elif newtime >= 18 and newtime <= 19:
        print('dinner time')
    else:
        pass

def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes) / 60
    converted = float(hours) + minutes
    return converted

if __name__ == "__main__":
    main()
