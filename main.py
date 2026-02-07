from datetime import datetime, timedelta, date
import random
import re
from typing import Dict, List


#SRART TASK 1
TASK1_BIRTHDAY_PATTERN = "%Y-%m-%d"
def get_days_from_today(date_str:str) -> int:
    today = datetime.today().date()
    try:
        input_date = datetime.strptime(date_str, TASK1_BIRTHDAY_PATTERN).date()
    except ValueError as exc:
        raise ValueError("Expected date in YYYY-MM-DD format (e.g. 2026-02-05).") from exc
    return (input_date - today).days

input_string = "2026-02-04"
task1_result = get_days_from_today(input_string)
print(f"Number of days between today {input_string} is: {task1_result}")
#END TASK 1


#START TASK 2
def get_numbers_ticket(min_input:int, max_input:int, quantity_input:int) -> list[int]:
    def validate_input(min_param, max_param, quantity_param):
        if min_param < 1:
            raise ValueError("Min must be greater than 0")
        if max_param > 1000:
            raise ValueError("Max must be less than 1000")
        if (quantity_param < min_param) or (quantity_param > max_param):
            raise ValueError("Quantity must be between min and max")

    validate_input(min_input, max_input, quantity_input)

    input_range = list(range(min_input, max_input + 1))
    random_choices = random.choices(input_range, k=quantity_input)
    return sorted(set(random_choices))

task2_min_input = 4
task2_max_input = 100
task2_quantity_input = 4
task2_result = get_numbers_ticket(task2_min_input, task2_max_input, task2_quantity_input)
print(f"Number of tickets between {task2_min_input} and {task2_max_input} is: {task2_result}")
#END TASK 2


#START TASK 3
# Checks if input string (with possible spaces leftwards) starts with "+"
RE_STARTS_WITH_PLUS = r"^\s*\+"

# Removes all symbols except number and "+" sign
RE_KEEP_DIGITS_AND_PLUS_ONLY = r"[^\d+]"
RE_NON_DIGIT = r"\D"

def normalize_phone(phone_number: str) -> str:
    has_plus_prefix = bool(re.match(RE_STARTS_WITH_PLUS, phone_number))

    digits = re.sub(RE_NON_DIGIT, "", phone_number)

    if digits.startswith("380"):
        return "+" + digits

    if has_plus_prefix:
        return "+" + digits

    return "+38" + digits

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
#END TASK 3



#TASK 4
TASK4_BIRTHDAY_PATTERN = "%Y.%m.%d"
def get_upcoming_birthdays(users:List[Dict[str, str]]) -> List[Dict[str, str]]:
    def get_greeting_date(user_birthday:date) -> date:
        today = datetime.today()
        greeting_date = user_birthday.replace(year=today.year)

        is_saturday = greeting_date.weekday() == 5
        is_sunday = greeting_date.weekday() == 6
        if is_saturday:
            greeting_date = greeting_date + timedelta(days=2)
        elif is_sunday:
            greeting_date = greeting_date + timedelta(days=1)

        birthday_happened = (today.month > user_birthday.month) and (today.day > user_birthday.day)
        if birthday_happened:
            greeting_date = greeting_date.replace(year=today_year + 1)

        return greeting_date


    today_year = datetime.today().year
    out: List[Dict[str, str]] = []
    for user in users:
        user_birthday_date = datetime.strptime(user.get("birthday"), TASK4_BIRTHDAY_PATTERN).date()
        greeting_date_result = get_greeting_date(user_birthday_date)

        out.append({
            "name": user.get("name"),
            "congratulation_date": greeting_date_result.strftime(TASK4_BIRTHDAY_PATTERN)
        })
    return out

users_input = [
    {"name": "", "birthday": "2006.02.07"},
    {"name": "Jane Smith", "birthday": "2007.02.10"}
]
task4_result = get_upcoming_birthdays(users_input)
print("Cписок привітань на цьому тижні:", task4_result)

# RESPONSE:
# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
# ]



#END TASK 4