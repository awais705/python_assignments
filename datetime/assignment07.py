import pytz
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".
dt = date.today()
print(dt)

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".
dt = "01/09/2023"
new_dt = datetime.strptime(dt, "%m/%d/%Y")
print(new_dt)

# Write a program that takes a birth year as input and calculates the age of a person.
birth_year = int(input("Enter your birth year: "))
dt = date.today()
year = dt.year
print(f"Person age is : {year - birth_year} years ")


# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# b_day = input("Enter your date of birth in YYYY-MM-DD format: ")
b_day = "1988-06-06"
b_day_obj = datetime.fromisoformat(b_day)

current_dt = datetime.today()

year = current_dt.year
if current_dt.month <= b_day_obj.month:
    if current_dt.day > b_day_obj.day:
        year += 1
else:
    year += 1

next_birthday = b_day_obj.replace(year=year)
diff = next_birthday - datetime.now()
print(f"{diff.days} remaining in your next birthday")

# Write a program that calculates and displays the number of days between two given dates.
dt_1 = datetime.now()
dt_2 = dt_1.replace(month=7)

diff = dt_1 - dt_2
print(f"Difference between two dates are {diff.days}")

# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).
dt = "2023-09-02"
dt_obj = datetime.fromisoformat(dt)
day_name = datetime.strftime(dt_obj, "%A")
print(day_name)


# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

year = int(input('Enter year: '))
month = int(input('Enter Month: '))


day = 1
new_dt = date(day=day, month=month, year=year)

next_month_dt = new_dt + relativedelta(months=1)

no_days = (next_month_dt - new_dt).days
print(f"Number of days are : {no_days}")


# Create a function that takes a starting date and a number of days as input, and then calculates
# and prints the date that is the specified number of days in the future.


def cal_print_date(date, number):
    starting_date = input("Please provide input date in YYYY-MM-DD format : ")
    num_days = int(input("Enter number of days to add: "))

    s_date = datetime.fromisoformat(starting_date)
    for i in range(s_date.day-1, num_days+1):
        new_date = s_date + timedelta(i)
        print(new_date)


cal_print_date("2023-09-02", 10)


# Write a Python program that uses the datetime module to print the current date and time.
current_dt = datetime.now()
print(current_dt)

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".
format_1 = "09/02/2023"
# format_1_obj = datetime.
format_2 = datetime.strptime(format_1, "%m/%d/%Y")
print(format_2)

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string
# formats it as "YYYY-MM-DD HH:MM:SS".


def convert_datetime(dt):
    new_dt = datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
    print(f"Format has changed: {new_dt}")


convert_datetime("09/02/2023 20:20:20")


# Write a program that calculates the time difference between two given datetime objects and displays it in hours
# , minutes, and seconds.
dt1 = datetime.now()
# dt2 = datetime.now()

dt2 = dt1 - timedelta(minutes=30)

diff = dt1 - dt2
print(f"Total seconds are : {diff.seconds}")
print(f"Total Minutes  are : {diff.seconds / 60}")
print(f"Total Hours are : {diff.seconds / 3600}")


# Create a function that takes a datetime object and a number of hours as input,
#  then returns a new datetime object with the added hours.

def new_date(obj, hours):
    new_obj = obj + timedelta(hours=hours)
    return new_obj


dt_new = new_date(datetime.now(), 1)
print(dt_new)


# Write a program that takes a date string in the format "MM-DD-YYYY" as input and
#  converts it to a datetime object using strptime().

date_one = input("Enter date in MM-DD-YYYY format: ")
date_one_obj = datetime.strptime(date_one, "%m-%d-%Y")

print(date_one_obj)


# Create a function that takes a datetime object as input and formats it as
#  "Month Day, Year" (e.g., "August 25, 2023") using strftime().

def date_time_format(obj):
    return datetime.strftime(obj, "%B %d, %Y")


new_format = date_time_format(datetime.now())
print(new_format)


# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00"
# hint: https://strftime.org/

date_str = "26-08-2023 15:18:33.983780-07:00"
# date_obj = datetime.fromisoformat(date_str)
date_str_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S.%f%z")

print(date_str_obj)


# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

new_str = "08-26-2023 08:10:00 PM"
new_str_obj = datetime.strptime(new_str, "%m-%d-%Y %H:%M:%S %p")

print(new_str_obj)


# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/

dt_str = "8-August-23 08:10:00"
dt_str_obj = datetime.strptime(dt_str, "%d-%B-%y %H:%M:%S")

print(dt_str_obj)


# create a current datetime and then displays it in the format "HH:MM AM/PM"
curr_dt = datetime.now()
new_curr_dt = datetime.strftime(curr_dt, "%H:%M %p")

print(new_curr_dt)


# Write a program that takes a user-entered date in the format
#  "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

user_entered_date = "06/06/2023"
new_dt = datetime.strptime(user_entered_date, "%m/%d/%Y")

print(new_dt)


# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

def day_name_from_date(obj):
    return datetime.strftime(obj, "%A")


day_name = day_name_from_date(datetime.now() + timedelta(days=5))
print(day_name)


# Create a function that takes a datetime object as input and formats it as
# "Day-Month-Year" (e.g., "25-August-2023") using strftime().

def date_time_format_new(obj):
    return datetime.strftime(obj, "%d-%B-%Y")


# Create a function that takes a timezone name as input and prints the
#  current date time object in that timezone.
def add_timezone_details(timezone="Asia/Karachi"):
    date_with_tz = datetime.now(tz=pytz.timezone(timezone))
    return date_with_tz


tz_aware_date = add_timezone_details("Asia/Dubai")
print(tz_aware_date)

new_format1 = date_time_format_new(datetime.now())
print(new_format1)


# Write a program that converts a given date time (tz aware)
# string from one timezone to another.
dt_without_tz = datetime.now()
timezone_details = pytz.timezone("Asia/Karachi")
dt_with_tz = timezone_details.localize(dt_without_tz)
print(dt_with_tz)

# changing it to Turkey
# print(pytz.all_timezones)
dt_with_tz_new = pytz.timezone("Turkey")
change_tz = dt_with_tz.astimezone(dt_with_tz_new)

print(change_tz)

# Write a program that takes a datetime object (naive) and a timezone name as input,
#  and returns a localized datetime object in the specified timezone.

dt_naive = datetime.now()
timezone = "Europe/Amsterdam"

tz_details = pytz.timezone(timezone)
dt_aware_timezone = tz_details.localize(dt_naive)

print(dt_aware_timezone)


# Create a function that takes a timezone name and a number of hours as input,
# and prints the current time plus the specified hours in that timezone

def update_timezone(timezone, no_of_hours):
    curr_date = datetime.now()
    tz_details = pytz.timezone(timezone)
    tz_aware_date = tz_details.localize(curr_date)
    tz_aware_date_with_hours = tz_aware_date + timedelta(hours=no_of_hours)
    return tz_aware_date_with_hours


update_tz = update_timezone("America/Noronha", 1)
print(update_tz)
