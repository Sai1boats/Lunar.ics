from datetime import date

from ics import Calendar, Event


def add_event(cal: Calendar, name: str, data_list):
    summary = name + '的生日'
    for dates in data_list:
        event = Event()
        event.name = summary
        event.begin = date(year=int(dates[0:4]), month=int(dates[5:7]), day=int(dates[8:10]))
        event.make_all_day()
        cal.events.add(event)
    return cal


