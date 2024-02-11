from datetime import date, datetime, timedelta

USERS = [{"name": "John", "birthday": date(year=2023, month=12, day=31)},
         {"name": "Doe", "birthday": date(year=2024, month=1, day=1)}, 
         {"name": "Alice", "birthday": date(year=2023, month=12, day=29)},  
         {"name": "Till", "birthday": date(year=2004, month=11, day=9)},
         {"name": "Jan", "birthday": date(year=2005, month=11, day=10)},
         {"name": "A", "birthday": date(year=2006, month=11, day=10)},
         {"name": "B", "birthday": date(year=2007, month=1, day=1)},
         {"name": "C", "birthday": date(year=2008, month=12, day=31)},
         {'name': 'Alice', 'birthday': date(year=2008, month=12, day=29)},
         ]

def get_birthdays_per_week(users):
    WEEKDAYS = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    
    date_today = date.today()
    day_today = date_today.strftime('%A')         # строка день неділі
    
    td_0 = timedelta(days=0) 
    td_7 = timedelta(days=7)
    
    this_year = False

    if not users: # +
        return {}

    for el in users:
        if el['birthday'].month == 1 and el['birthday'].day <= 7:   # and el['birthday'].year > date_today.year: 
            el['birthday'] = el['birthday'].replace(year=date_today.year + 1)
            time_delta = el['birthday'] - date_today
            if time_delta <= td_0:                                          # д.н. які минуль
                continue
            elif time_delta >= td_7:                                    # д.н. які ще  будуть 
                continue
            elif td_0 < time_delta < td_7:
                day_birthday = el['birthday'].strftime('%A')
                if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                    WEEKDAYS["Monday"].append(el["name"])
                else:
                    WEEKDAYS[day_birthday].append(el["name"])
    
        el['birthday'] = el['birthday'].replace(year=date_today.year)
        month_delta = el['birthday'].month - date_today.month
       
        if month_delta < 0: # +
            continue
        elif month_delta > 0: # +
            this_year = True
            continue
        if month_delta == 0:
            day_delta = el['birthday'].day - date_today.day
            if day_delta <= 0:
                continue
            elif 0 < day_delta <= 7:
                if day_today == 'Monday':
                    day_birthday = el['birthday'].strftime('%A') # зміна року
                    if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                        continue
                    else:
                        WEEKDAYS[day_birthday].append(el["name"])
                else:
                    day_birthday = el['birthday'].strftime('%A') # зміна року
                    if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                        WEEKDAYS["Monday"].append(el["name"])
                    else:
                        WEEKDAYS[day_birthday].append(el["name"])
    
    greeting = {key: value for key, value in WEEKDAYS.items() if value} # +
    if not greeting and this_year == False: # +
        return {} # +
    else:
        return greeting


print(get_birthdays_per_week(USERS))

# функція повертає словник користувачів- {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
