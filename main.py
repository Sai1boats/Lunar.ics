import csv

from ics import Calendar

import add_event
import get_gregorian_time

if __name__ == '__main__':
    cal = Calendar()
    names = []
    birthdays = []
    while True:
        name = input("请输入寿星姓名，输入*退出:\n")
        if name == "*" or name == '':
            break
        birthday = input("请输入寿星生日，格式为yyyy/mm/dd:\n")
        if (2099 >= int(birthday[0:4]) >= 1900) and (12 >= int(birthday[5:7]) >= 1) and (1 <= int(birthday[8:10]) <= 31)and(birthday[4:5]==birthday[7:8]=='/'):
            names.append(name)
            birthdays.append(birthday)
        else:
            print('日期格式错误')
            break


    with open('calendar_edited.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        gregorianlist = []
        lunarlist = []
    for row in rows:
        gregorianlist.append(row[0])
        lunarlist.append(row[1])

    for i in range(len(names)):
        gregorian_date = get_gregorian_time.find_gregorian_date(lunarlist=lunarlist, gregorianlist=gregorianlist,
                                                                gregorian=birthdays[i])
        cal = add_event.add_event(cal, names[i], gregorian_date)

    # 保存ICS文件
    with open('result/my_calendar.ics', 'wb') as f:
        f.write(cal.serialize().encode())
