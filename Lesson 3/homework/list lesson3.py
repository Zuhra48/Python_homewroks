# Task 3.10
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]

list1[-1:] = list2

print('Result:',list1)

# Task 1.1
cardinal_numbers = ('first','second','third')
cardinal_numbers

#Task 1.2
cardinal_numbers = ('first','second','third')

print(cardinal_numbers[1])

# Task 1.3
position1,position2,position3 = ('first','second','third')
position1,position2,position3

# Task 1.4
my_name = tuple('Zuhra')
my_name

# Task 1.5
my_name = tuple('Zuhra')
print('x' in my_name)


# Task 1.6
my_name = tuple('Zuhra')
new_tuple = my_name[1:]
print(new_tuple)

# Task 2.1
Food = ['rice','beans']
Food

# Task 2.2
Food = ['rice','beans']
Food.append('broccoli')
print(Food)

# Task 2.3
Food = ['rice','beans','broccoli']
Food.extend(['bread','pizza'])
print(Food)

# Task 2.4
Food = ['rice','beans','broccoli','bread','pizza']
print(Food[:2])

# Task 2.5
Food = ['rice','beans','broccoli','bread','pizza']
print(Food[3:])

# Task 2.6
Breakfast = 'eggs,fruit,orange,juice'.split(',')
print(Breakfast)

# Task 2.7
Breakfast = 'eggs,fruit,orange,juice'.split(',')
print(len(Breakfast) ==3)

# Task 2.8
Breakfast = ['eggs','fruit','orange','juice']
lengths = [len(item) for item in Breakfast]
print(lengths)

# Task 3.1
numbers = [59,65,5,22,10,86]
smallest_number = min(numbers)

print(smallest_number) 


# Task 3.2
colors = ['red','green','white','black','pink','yellow']
new_colors = [color for i,color in enumerate(colors) if i not in[0,4,5] ]

print(new_colors)

# Task 3.3
list1 = [1,2,3,4,5,6]
list2 =[4,5,6,7,8,9]

difference1 = list(set(list1) - set(list2)) 
difference2 = list(set(list2) - set(list1))

total_difference =difference1 + difference2

print('list1 and list2 difference between:',total_difference)


# Task 3.4
items = ['apple','banana','cherry','date','fig']
item_to_find = 'banana'
index = items.index(item_to_find)

print(f"Index of '{item_to_find}':{index}")

# Task 3.5
list1 = [12,14,18]
list2 = [25,34,16]

list2.append(list1)
print("updated list2:",list2)

# Task 3.6
numbers = [4,16,32,13,54,98,33]
smallest_number =sorted (numbers)
second_smallest = smallest_number[1]
print(second_smallest)



# Task 3.7
list1 = [4,6,4,8,1,9]
list2 = [4,8,3,11,16]

common_items = list(set(list1) & set(list2))

print(common_items)


# Task 3.8
my_list = [10,20,30]
a,b,c = my_list

print("a:", a)
print("b:", b)
print("c:", c)

# Task 3.10
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]

list1[-1:] = list2

print('Result:',list1)
