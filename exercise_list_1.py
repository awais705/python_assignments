# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc

print("\n 1. output the numbers from 1 to 10 using range function and for loop")
for i in range(1, (10+1), 1):
    print(i)


# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc

print("\n 2. output the numbers from 35 to 50 using range function and for loop")
for i in range(35, 51, 1):
    print(i)


# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

print("\n 3. output the numbers from -15 to -25 using range function and for loop")

for i in range(-15, -26, -1):
    print(i)


# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

print("\n 4. output the numbers from 5 to -10 using range function and for loop")
for i in range(5, -11, -1):
    print(i)


# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

print("\n 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop")
for i in range(0, 51, 3):
    print(i)

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

print("\n 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop")
for i in range(1, 11, 1):
    print(f"{2} x {i} = {2*i}")


# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

print(
    "\n 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]")

num_list = [3, 5, 2, 1, 4]
x = 0
for i in num_list:
    x += i
print(f" \n Sum of all numbers are {x}")


# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

num_list_1 = [3, 5, 2, 1, 4]
print(
    "\n 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]")
x = 0
for i in num_list_1:
    if i > x:
        x = i

print(f"\n Largest number is : {x}")
