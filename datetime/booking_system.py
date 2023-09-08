import pytz
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function
# that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
  "car_model": "", # corolla, civic
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00
# " as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration


store_booking = []

# checking if slot available using start date , end date and car model number


def is_slot_available(start_date, end_date, car_model):

    for individual in store_booking:

        if individual["start_date"] == start_date and individual["end_date"] == end_date:
            # print(individual.get("car_model"))
            car_list = list(individual.get("car_model").split(","))
            model_exist = car_list.count(car_model)
            if model_exist > 0:
                return False
    else:
        return True


def add_tz(dt, timezone):
    return timezone.localize(dt)


def convert_tz(dt, timezone):
    return dt.astimezone(timezone)


print(">>>>>>>>>> Welcome to ABC Hotel Booking System <<<<<<<<<< \n")
for i in range(1, 5):
    start_date = input("Enter Start Date: ")
    end_date = input("Enter End Date: ")
    timezone = input("Enter timezone: ")
    car_model = input("Enter Car Model: ")

    start_date = datetime.fromisoformat(start_date)
    end_date = datetime.fromisoformat(end_date)

    timezone_set = pytz.timezone(timezone)

    # set time zone aware
    start_date_tz_aware = add_tz(start_date, timezone_set)
    end_date_tz_aware = add_tz(end_date, timezone_set)

    utc_timezone = pytz.timezone("UTC")

    # Update start date timezone
    utc_start_date = convert_tz(start_date_tz_aware, utc_timezone)
    utc_end_date = convert_tz(end_date_tz_aware, utc_timezone)

    # print(utc_start_date, utc_end_date)

    # Check booking exist
    match = is_slot_available(utc_start_date, utc_end_date, car_model)
    # print(match)
    if match == True:
        store_booking.append({
            "start_date": utc_start_date,
            "end_date": utc_end_date,
            "car_model": car_model
        })
        print("Booking Successful")

    else:
        print("Slot Already Booked")
        continue


# print(store_booking)
