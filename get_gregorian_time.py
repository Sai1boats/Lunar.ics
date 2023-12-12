import csv


def find_gregorian_date(lunarlist: list, gregorianlist: list, gregorian: str):
    l = gregorianlist
    i = l.index(gregorian)
    lunar_date = lunarlist[i]
    print('农历为', lunar_date)
    indices = [i for i in range(len(lunarlist)) if lunarlist[i] == lunar_date]
    gregorian_date = []
    for i in indices:
        if int(gregorianlist[i][0:4]) >= int(gregorian[0:4]):
            gregorian_date.append(gregorianlist[i])

    return gregorian_date

