# Write a Python program to copy a list using for loop. consider a list
# li = [1, 2, 3, 4]
# li_2 = []
# use for loop and add al the items in li_2


li = [1, 2, 3, 4]
li_2 = []

for i in li:
    li_2.append(i)

print(li_2)


# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop

l1 = [1, 2, 15, 4]
l2 = [5, 6, 7, 15]

# Function to check both lists


def check_lists(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True


print(check_lists(l1, l2))


# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output:
# 0 100
# 1 200
# 2 300
# 3 400

list3 = [100, 200, 300, 400]

for i, j in enumerate(list3):
    print(i, j)


# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']


result = {}
for i in l1:
    if not i in result:
        result[i] = 1
    else:
        result[i] += 1

    for j in l2:
        if i == j:
            # pass
            result[i] += 1
            # print(i, result[i])

        # elif not j in result:
        #     # print(i, j)
        #     # pass
        #     print(j)
        #     # pass
        #     # result[j] = 1
        #     # print(result[j])

        else:
            # print(i)
            pass
            # result[j] += 1


# print(result)


# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

y = x = 2783363
count = 0
while x > 0:
    x = x // 10
    count += 1
    # print(x)


print(f"total digits in {y} are {count}")


# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”


input_val = int(input("Please provide input from 1 to 10 and 0 for quit: "))

while input_val != 0:
    input_val = int(
        input("Please provide input from 1 to 10 and 0 for quit: "))


# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

list1 = []
sum = 0
i = 5

while i > 0:
    user_input = int(input("Please Input number: "))
    list1.append(user_input)
    sum += user_input
    i -= 1

print(f"list1 values updated : {list1} and sum of all is {sum}")


# Write a program to keep asking for a number until you enter a negative number.
#  At the end, print the sum of all entered numbers.

input_neg = int(input("Input Number, Type negative number to Quit "))
sum_of_all_numbers = 0
while input_neg > 0:
    input_neg = int(
        input("Please Input Number, Type negative number to Quit "))
    sum_of_all_numbers += input_neg

print(f"Sum of all numbers are {sum_of_all_numbers}")


# Write a program to ask for a name until the user enters END.
#  Print the name each time. When you are done, print "I am done."


input_text = input("Enter your Name: ")
print(input_text)

while input_text != "END":
    input_text = input("Please input your name : ")
    if input_text != "END":
        print(input_text)

print("I am done")


# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

l1 = [11, 33, 50, 63, 96]
text = ""
for i in l1:
    text += str(i)

print(f"result is {text}")


# Write a Python program to copy a dict using for loop. consider a dict
d1 = {
    "id": 1,
    "name": "your-name",
    "gender": "male"
}
d2 = {}
# use for loop and add al the items in d2
for i, j in enumerate(d1.items()):
    d2.update({j[0]: j[1]})


print(d2)
