from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    WEEKDAYS = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    
    date_today = date.today()
    day_today = date_today.strftime('%A')         # строка день неділі
    
    td_0 = timedelta(days=0) 
    td_7 = timedelta(days=7)
    
    this_year = False
    
    if not users:
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
        time_delta = el['birthday'] - date_today
                
        if time_delta <= td_0:                                          # д.н. які минуль
            continue
        elif time_delta >= td_7:                                    # д.н. які ще  будуть 
            this_year = True
            continue
        elif  td_0 < time_delta < td_7:                             # д.н. цьго тижня  
            if day_today == 'Monday':
                day_birthday = el['birthday'].strftime('%A')
                if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                    continue
                else:
                    WEEKDAYS[day_birthday].append(el["name"])
                    
            else:
                day_birthday = el['birthday'].strftime('%A')
                if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                    WEEKDAYS["Monday"].append(el["name"])
                else:
                    WEEKDAYS[day_birthday].append(el["name"])

    if not WEEKDAYS and this_year == False:
        return {}
    else:
        greeting = {key: value for key, value in WEEKDAYS.items() if value}
        return greeting



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
