# Create a list of juices, add 5 items using append
juices_list = []
juices_list.append("strawberry")
juices_list.append("Apple")
juices_list.append("Avacado")
juices_list.append("Banana")
juices_list.append("Orange")

print(juices_list)

# Create a list of cars, add 5 items using insert
car_list = []
car_list.insert(0, "Tesla")
car_list.insert(1, "BMW")
car_list.insert(2, "Ford")
car_list.insert(2, "Mercedes-Benz")
car_list.insert(2, "Honda")


print(car_list)


# Remove last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]	using pop and len

# output should display [‘bed’, ‘table’, ‘chair’]

list_house_items = ["bed", "table", "chair", "sofa"]
list_house_items.pop(len(list_house_items)-1)

print(list_house_items)

# Remove second last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] by len and index

# output should display [‘bed’, ‘table’, ‘sofa’]
list_house_items1 = ["bed", "table", "chair", "sofa"]
list_house_items1.pop(len(list_house_items1)-2)

print(list_house_items1)


# Remove first item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]

# output should display [‘table’, ‘chair’, ‘sofa’]

list_house_items2 = ["bed", "table", "chair", "sofa"]
list_house_items2.pop(0)

print(list_house_items2)


# Remove the item “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]

# output should display [‘bed’, ‘table’, ‘sofa’]

list_house_items3 = ["bed", "table", "chair", "sofa", "chair"]
# list_house_items3.filter("chair", list_house_items3)

for i in list_house_items3:
    if i == "chair":
        list_house_items3.remove(i)


print(list_house_items3)


# Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]

# output should display [‘A’, “B”, “C”, “D”, “E”, “F”]

list1 = ["A", "B", "C"]
list2 = ["D", "E", "F"]

list1.extend(list2)

print(list1)


# Write a Python program to check if a list is empty or not.
check_list = ['Awais']

if len(check_list) > 0:
    print("List is not empty")
else:
    print("List is empty")
