# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# hint: use a variable x outside the loop and assign the first value of list
# inside the loop * the value of x with the local variable of loop
# x *=

print(
    "\n 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].")
num_list_2 = [3, 5, 2, 1, 4]
x = 1
for i in num_list_2:
    x *= i

print(f"\n Multiplication of all numbers are {x}")


# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop

print("\n 2. create a list from 0 to 100 using range function and iterate over the list")
for i in range(0, 100):
    if i > 30 and i < 50:
        continue

    if i > 80:
        break

    if i % 5 == 0:
        print(f"{i} is divisible by 5")


# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

print(
    "\n 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']")
animal_list = ['cat', 'dog', 'hand', 'freedom',
               'jump', 'frog', 'happy', 'popcorn', 'tiger']

for i in animal_list:
    if len(i) > 5:
        print(f"{i}")

# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

print(
    "\n 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']")
list_one = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list_new = []

for i in range(len(list_one)):
    if i == 0 or i == 4 or i == 5:
        continue
    else:
        list_new.append(list_one[i])


print(list_new)


# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

print("\n 5. Write a program to display odd numbers only. odd number upto 100")
for i in range(2, 101, 2):
    print(i)


# 6. List contains 30 elements. Display first 5 and last 5 elements
print("\n 6. List contains 30 elements. Display first 5 and last 5 elements")

list_2 = list(range(31))

for i in range(len(list_2)):
    if (i < 5) or (i >= (len(list_2)-5)):
        print(list_2[i])


# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# output should be 'helloworld' in one line

print(
    "\n 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]")
hello_world = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
text = ''
for i in hello_world:
    text += i

print(text)


# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2


print("\n 8. Write a Python program to append a list to the second list.")
l1 = [1, 2, 3, 4, 5]
l2 = []

for i in l1:
    l2.append(i)

print(l2)


# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3

print(
    "\n 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']")

text_list = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
count = 0

for i in text_list:
    if i == "hi":
        count += 1

print(f"Hi present in list {count} time(s)")
