# 1.Generate a list of 100 random numbers
import random
import math
random.seed(14)
rand_nums=[]
counter=100
while counter>0:
    rand_nums.append(random.randint(0,100))
    counter-=1

print(rand_nums)
max_num=max(rand_nums)
min_num=min(rand_nums)
avg_num=sum(rand_nums)/len(rand_nums)
print(max_num,min_num,avg_num)

even_counter=0
odd_counter=0
for num in rand_nums:
    if num%2==0:
        even_counter+=1
    else:
        odd_counter+=1
print(even_counter,odd_counter)


# 2.Simulate a student database using dictionaries
"""
Student = {name, age, grade}

Create a list of 20 students
"""
import random
random.seed(123)
students=[]
for i in range(1,21):
    student={'name':f'student{i}'
             ,'age':random.randint(17,22),
             'grade':random.randint(60,100)}
    students.append(student)

# print(students)

# Filter: students with grade > 85
filtered_students=[]
for st in students:
    if st['grade']>85:
        filtered_students.append(st)

#print(filtered_students)
from operator import itemgetter
sorted_list=sorted(students,key=itemgetter('grade'))

#print(sorted_list)
"""
Make a mini program:
“Grocery System”

Add item

Remove item

View items

Exit
(Loops + functions + dicts)
"""
"""
## Before refactoring with chat gpt missed a little bit of handling and ux 
def add_item(my_list):
    name=input("please enter the product name")
    pricy=int(input('Please enter the price of the product'))
    quan=int(input('Please enter the quantity of the product'))
    
    product={'product_name':name,
              'price':pricy,
              'quantity':quan}
    my_list.append(product)

def remove_item(my_list,index):
    try:
        my_list.pop(index)
    except IndexError:
        print('error!')

def view_item(my_list):
    if len(my_list) != 0:
        for item in my_list:
            print(item)
    else: print('the list is empty')

shelf=[]
flag=True
while flag:
    option=int(input('please enter 1 to add an item , 2 to remove an item, 3 to view the items we got , 4 to exit'))
    if option==1:
        add_item(shelf)
    elif option==2:
       index=int(input('Please enter the index of the item u want to delete'))
       remove_item(shelf,index)
    elif option==3:
        view_item(shelf)
    elif option==4:
        flag=False
        break;
    else:
        print('please enter a number from 1 to 4')
"""
## After refactoring with chat gpt
def add_item(shelf):
    # Get product info
    name = input("Product name: ")
    
    try:
        price = float(input("Product price: "))
        quantity = int(input("Product quantity: "))
    except ValueError:
        print("Invalid input! Price and quantity must be numbers.")
        return  # do nothing and exit function

    product = {
        'product_name': name,
        'price': price,
        'quantity': quantity
    }

    shelf.append(product)
    print("✓ Item added successfully!")


def remove_item(shelf):
    if len(shelf) == 0:
        print("Shelf is empty, nothing to remove!")
        return

    # Show items with indices
    for i, item in enumerate(shelf, start=1):
        print(f"{i}) {item}")

    try:
        index = int(input("Enter item number to remove: ")) - 1
        shelf.pop(index)
        print("✓ Item removed successfully!")
    except (ValueError, IndexError):
        print("Invalid index! Please choose a valid item number.")


def view_items(shelf):
    if len(shelf) == 0:
        print("Shelf is empty.")
        return
    
    print("\n--- ITEMS ON THE SHELF ---")
    for i, item in enumerate(shelf, start=1):
        print(f"{i}) Name: {item['product_name']}, Price: {item['price']}, Quantity: {item['quantity']}")


def print_menu():
    print("\n----- MINI MARKET MENU -----")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")
    print("----------------------------")


# MAIN PROGRAM
shelf = []
running = True

while running:
    print_menu()

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if option == 1:
        add_item(shelf)
    elif option == 2:
        remove_item(shelf)
    elif option == 3:
        view_items(shelf)
    elif option == 4:
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice, enter a number from 1 to 4.")



##Mini Challenge 
"""“Find the first duplicate number in a list.”
Example: [4,3,5,2,3,4] → returns 3
"""
test=[4,3,5,2,3,4]
found=False
for num in test:
    if not found:
        for num2 in test:
            if num==num2:
                found=True
                break
    else: 
        print(num)
        break