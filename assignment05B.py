# Write a program to create a function that takes two arguments,
#  name and age. print them inside function.


def print_info(name, age):
    print(f"Name is {name} and age is {age} ")


print_info("Awais", 34)


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print(f"Employee name is {name} and his/her salary is {salary}")


show_employee("Awais", 150000)
show_employee("Awais")


# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

a = 4
b = 8
c = 10
d = 12

arr_val = []


def make_list_from_values(i, j, k, l):
    arr_val.append(i)
    arr_val.append(j)
    arr_val.append(k)
    arr_val.append(l)
    return arr_val


print(make_list_from_values(k=c, i=a, l=d, j=b))


# Write a function called km_to_miles that takes kilometers as a parameter,
# converts it into miles and returns the result.

def km_to_miles(km):
    # 1km = 0.62137119 miles
    return km * 0.62137119


total_km = int(km_to_miles(5))
print(total_km)


# Write a function called is_divisable_by_11 that takes an integer as an
# parameter and returns whether it is divisible by 11 or not.

def is_divisible_by_11(num):
    if num % 11 == 0:
        return "Divisible"
    else:
        return "Not Divisible"


num = 23
check_divisible = is_divisible_by_11(num)
print(f"{num} is {check_divisible} to 11")


# Write a function called get_highest that takes 2 numbers as parameters and returns
#  the highest of the 2 numbers.

def get_highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


highest = get_highest(36, 85)
print(f"{highest} number is highest")


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg
# and "fuel_per_liter" as optional arg that has default value to 280. The function should return the cost in Rs.

def fuel_cost(distance, fuel_per_liter=280):
    return round(distance / fuel_per_liter, 2)


cost = fuel_cost(50, 280)
print(f"The cost of 1 Km is Rs.{cost}")


# Write a function called is_valid_email  that takes an email address as an argument and
# returns True/False depending on whether it is a valid email address.

# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false

def is_valid_email(email):
    # Maximum 256 characters
    if len(email) > 256:
        return False

    # # # Must contain an @ symbol
    if "@" not in email:
        return False

    # # rfind() last position
    # # Must start with a letter or a number
    if not email[0].isalnum() or not email[0].isalpha():
        return False

    # if email.find("@")
    position = email.rfind("@")
    # print(position, len(email))
    if position + 1 == len(email):
        return False

    # Must contain at least 1 character before the at symbol
    if position <= 0:
        return

    dot_position = email.rfind(".")
    # Must contain at least 1 character after the last period(.).
    if dot_position + 1 == len(email) or dot_position == -1:
        return False

    return True


email_address = "awais705@gmail.com"
valid_email = is_valid_email(email_address)

if valid_email == True:
    print(f"Congratulation! {email_address} is valid")
else:
    print(f"Unfortunately! {email_address} is not valid")
