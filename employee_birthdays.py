from datetime import datetime
from collections import defaultdict

WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
}

USERS_DATA = [
    {"name": "Bill Gates", "birthday": datetime(1993, 5, 24)},
    {"name": "Nick Hill", "birthday": datetime(1978, 12, 13)},
    {"name": "John Doe", "birthday": datetime(1978, 12, 16)},
    {"name": "Kate Peterson", "birthday": datetime(1978, 12, 7)},
    {"name": "Julia Ferguson", "birthday": datetime(1978, 12, 9)},
    {"name": "Mike Smith", "birthday": datetime(1978, 12, 6)},
    {"name": "Conor Parker", "birthday": datetime(1978, 12, 6)},
]


def get_weekday(day_number):
    if day_number > 4:
        return WEEKDAYS[0]

    return WEEKDAYS[day_number]


def get_birthdays_per_week(users):
    result = defaultdict(list)
    current_date = datetime.today().date()

    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            weekday = get_weekday(birthday_this_year.weekday())
            result[weekday].append(user["name"])

    for weekday, birthdays in result.items():
        print(f"{weekday}: {", ".join(birthdays)}")


get_birthdays_per_week(USERS_DATA)