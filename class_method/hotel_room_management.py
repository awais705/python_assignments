# OOP videos creating 2 real programs using OOP
# https://www.youtube.com/watch?v=Ej_02ICOIgs - Inventory Management Example
# https://www.youtube.com/watch?v=PMFd95RgIwE - Banking App Example


"""
Design a hotel room managment system

Requirement:
1. I should be able to add hotel info i.e name and address
2. I should be able to add new room info i.e name, num_of_beds, fare_per_day
3. I should be able to book a room for a user/person/account for today and future dates (ignore timezone)
4. I should be able to view the few stats i.e total rooms, total room occupied today, total rooms available today
5. I should be able to check if room is available on future date

Design a good model. Its a simple requirment there will no need to use inheritance
"""

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class Room:
    hotel_name = ""
    hotel_address = ""
    occupied = 0
    r_number = 0

    def __init__(self, name: str, num_of_beds: int = 0, fare_per_day: int = 0, start_date="", end_date=""):

        assert num_of_beds > 0, f"Bed count can't be zero or less"
        assert fare_per_day > 0, f"Fare per day can't be zero or less"

        Room.r_number += 1
        self.__rnum = Room.r_number
        self.name = name
        self.num_of_beds = num_of_beds
        self.fare_per_day = fare_per_day
        self.start_date = start_date
        self.end_date = end_date

    @property
    def room_number(self):
        return self.__rnum

    @staticmethod
    def update_hotel_info(name: str, address: str):
        assert len(name) > 0, f"Hotel Name can't be empty"
        assert len(address) > 0, f"Hotel Address can't be empty"

        Room.hotel_name = name
        Room.hotel_address = address

        print(f"\n >>>>>>>>>> Hotel info Updated succesfuly <<<<<<<<<<\n ")

    @staticmethod
    def display_hotel_info():
        print(f"Hotel Name: {Room.hotel_name} , Address: {Room.hotel_address}")

    @staticmethod
    def total_rooms():
        print(f"Total rooms in '{Room.hotel_name}' are {Room.r_number}")
        # print(Room.r_number)

    @staticmethod
    def convert_iso_format(dt):
        return datetime.fromisoformat(dt)

    # def __repr__(self):
    #     return f"Room('{self.name}',{self.num_of_beds},{self.fare_per_day})"

    def check_room_availability(self):

        print("\n>>>>>>>>>>CHECK ROOM AVAILABILIY <<<<<<<<<<\n")
        if self.start_date and self.end_date:
            print(
                f" '{self.name}' is available from {self.end_date + timedelta(days=1)}  onward. ")
        else:
            print(f" '{self.name}' is available from {datetime.today()}  onward. ")

    def book_a_room(self, booking_start_date, booking_end_date):
        if self.start_date and self.end_date:
            booking_start_date = self.convert_iso_format(booking_start_date)
            booking_end_date = self.convert_iso_format(booking_end_date)

            if booking_start_date <= self.start_date or booking_start_date <= self.end_date:
                print(
                    f"{self.name} is already booked for your desired dates! Room is available from {self.end_date + timedelta(days=1)}")
            else:
                self.start_date = booking_start_date
                self.end_date = booking_end_date

                # Occupied
                Room.occupied += 1

                print(f"\n\n>>>>>> Booking completed <<<<<")
                print(
                    f"{self.name} booked from {booking_start_date} to {booking_end_date}")

        else:
            self.start_date = self.convert_iso_format(booking_start_date)
            self.end_date = self.convert_iso_format(booking_end_date)

            # Occupied
            Room.occupied += 1
            print(f"\n\n>>>>>> Booking completed <<<<<")
            print(
                f"Congratulation! '{self.name}' , Room number '{self.room_number}' is booked from {booking_start_date} to {booking_end_date} ")


room1 = Room("Deluxe", 1, 1500)  # (room name, # of bed, fare per day)
room2 = Room("Suite", 1, 2000)
room3 = Room("Studio", 1, 2500)
room4 = Room("Presidential suite", 2, 3500)
room5 = Room("Executive suite", 1, 3000)
room6 = Room("Penthouse apartment", 2, 4000)
room7 = Room("Room only hotel rooms", 1, 2000)
room8 = Room("Standard suite rooms", 1, 2000)
room9 = Room("Balcony room in Hotel", 2, 3000)
room10 = Room("Double double room in hotel", 4, 3000)
room11 = Room("Double room in hotel", 2, 3000)
room12 = Room("Twin double room in hotel", 2, 3000)
room13 = Room("Presidential Suite hotel room", 1, 3000)
room14 = Room("Apartment style hotel bedroom", 1, 4000)
room15 = Room("Penthouse suite living room", 1, 3000)
room16 = Room("Quad bedroom", 3, 4000)


# print(Room.all.__repr__)

# Update Hotel info
Room.update_hotel_info(
    name="Rose Palace Hotel, Liberty",
    address="95-D-1, Near Mall-1, Main Boulevard Road, Gulberg III, Lahore., Gulberg, Lahore, 54000, Pakistan"
)

# Display Hotel info
Room.display_hotel_info()


# Get Room number
print(f"Your Room type is '{room3.name}' and number: {room3.room_number} ")


# Book a room
room10.book_a_room("2023-09-22", "2023-09-24")
# Trying to book an already booked room
room10.book_a_room("2023-09-24", "2023-09-28")


room11.book_a_room("2023-09-24", "2023-09-28")


# Check room availability
room10.check_room_availability()

# stats
# Get total rooms in Hotel
print(f"\n >>>>> Stats | {Room.hotel_name} <<<<< \n")
Room.total_rooms()


# total room occupied today
print(f"Total Occupied Rooms : {Room.occupied}")

# total rooms available today
Total_available = Room.r_number - Room.occupied
print(f"Total Available rooms are {Total_available}")
