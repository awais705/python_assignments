# Write a program to check whether a person is eligible to vote or not?

age = 19

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Write a program to check char is vowel or not.
character = "s"

if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
    print("Vowel")
else:
    print("Not a Vowel")


# Write a program to check the number is positive or negative. User input.
userInput = int(input("Type a number: "))

if userInput > 0:
    print("Positive Number")
else:
    print("Negative number")


# Write a program to check whether a number is odd or even?
checkNumber = int(input("Type a number to check Even or Odd:  "))

if checkNumber % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
mark_obtained = int(input("Enter Mark Obtained for Subject A out of 100 :  "))

if mark_obtained >= 80 and mark_obtained <= 100:
    print("A One Grade")
elif mark_obtained >= 70 and mark_obtained <= 79:
    print("A Grade")
elif mark_obtained >= 60 and mark_obtained <= 69:
    print("B Grade")
elif mark_obtained >= 50 and mark_obtained <= 59:
    print("C Grade")
elif mark_obtained >= 40 and mark_obtained <= 49:
    print("D Grade")
else:
    print("Failed")


# Write a program to check whether a number is divisible by 7

divisble_number = 21

if divisble_number % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")


# Write a program to check if year is leap year.

# search on google of what leap year is.

current_year = 2028

if current_year % 4 == 0:
    print(f"{current_year} Year is a Leap year")
else:
    print(f"{current_year} Year is not a leap year")


# Write a program to ask user its name and check whether name consists of 5 or more letters
user_name = input("Enter Your name: ")

if len(user_name) >= 5:
    print(f"{user_name} consist 5 or more letters")
else:
    print(f"{user_name} doesn't consist 5 or more letters")


# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly


input_one = int(input("Enter first Number: "))
input_two = int(input("Enter Second Number: "))
input_operator = input("Enter arithmatic Operator: ")

if input_operator == "+":
    print(f"Sum of two numbers are {input_one + input_two}")
elif input_operator == "-":
    print(f"Subtraction of two numbers are {input_one - input_two}")
elif input_operator == "/":
    print(f"Division of two numbers are {input_one / input_two}")
elif input_operator == "*":
    print(f"Multiplication of two numbers are {input_one * input_two}")
else:
    print("Invalid Operator entered")


# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
input_number = int(
    input("Enter Number to check if it is divisible by 2 and 3 both : "))

if input_number % 2 == 0 and input_number % 3 == 0:
    print(f"{input_number} is divisible by 2 and 3 both")
elif input_number % 2 == 0 or input_number % 3 == 0:
    if input_number % 2 == 0:
        print(f"{input_number} is only divisible by 2")
    else:
        print(f"{input_number} is only divisible by 3")
else:
    print(f"{input_number} is not eithe divisible by 2 and 3")


# Write a program that accepts 2 inputs from user and check which number is largest.
inp_one = int(input("Enter Number 1: "))
inp_two = int(input("Enter Number 2:"))

if inp_one > inp_two:
    print(f"{inp_one} is largest number")
else:
    print(f"{inp_two} is largest number")


# Write a program that accepts 3 input from user and check which number is largest.
inp_1 = int(input("Enter Number 1: "))
inp_2 = int(input("Enter Number 2: "))
inp_3 = int(input("Enter Number 3: "))


if (inp_1 > inp_2) and (inp_1 > inp_3):
    print(f"Input 1 - {inp_1} is greater")
elif (inp_2 > inp_1) and (inp_2 > inp_3):
    print(f"Input 2 - {inp_2} is greater")
elif (inp_3 > inp_1) and (inp_3 > inp_2):
    print(f"Input 3 -  {inp_3} is greater")


# Write a program that accepts 3 input from user and check the second is largest.
num_1 = int(input("Enter Number 1: "))  # 5
num_2 = int(input("Enter Number 2: "))  # 10
num_3 = int(input("Enter Number 3: "))  # 15

if ((num_1 > num_2) and (num_1 < num_3)) or ((num_1 < num_2) and (num_1 > num_3)):
    print(f"{num_1} is second largest")
elif ((num_2 > num_1) and (num_2 < num_3)) or ((num_2 < num_1) and (num_2 > num_3)):
    print(f"{num_2} is second largest")
elif ((num_3 > num_2) and (num_3 < num_1)) or ((num_3 < num_2) and (num_3 > num_2)):
    print(f"{num_3} is second largest")

 # Write a program to trace your subject mark. Your program should fulfill the following conditions:

# If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
# display "you are fail" if their mark is below 50.
# display "you are pass" if they score 50 and above.
# If subject mark is between 50 and 60, Remark: Good
# If subject mark is between 60 and 80, Remark: Very Good
# If subject mark is between 80 and 100, Remark: Outstanding


subject_marks = int(input("Enter Subject makrs :"))

if subject_marks < 0 and subject_marks > 100:
    print("error: mark should be between 0 and 100 only")


if subject_marks < 50 and subject_marks > 0:
    print("you are fail")
elif subject_marks >= 50:
    print("you are pass")


if subject_marks >= 50 and subject_marks <= 60:
    print("Remark: Good")
elif subject_marks >= 60 and subject_marks <= 80:
    print("Remark: Very Good")
elif subject_marks >= 80 and subject_marks <= 100:  
    print("Remark: Outstanding")
