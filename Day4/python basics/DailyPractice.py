"""
Goals for Python today:

Understand list comprehensions

Create short clean transformations using them

Use lambda + map + filter

Create your first custom module

"""

"""

📌 Tasks to complete

Task 1 — Convert these loops into comprehensions
nums = [1, 2, 3, 4, 5]

# a) square each number
# b) keep only even numbers
# c) convert each number to string

"""
nums=[1,2,3,4,5]
squared_nums=[x**2 for x in nums]
print(squared_nums)
even_nums=[x for x in nums if x%2==0]
print(even_nums)
str_nums=[str(x) for x in nums]
print(str_nums)
print(type(str_nums[0]))

"""
Task 2 — Lambda practice
Write lambdas for:

a) square a number

b) return last character of a string

c) check if number is even
"""

nums=[1,2,3,4,5]
square=lambda a: a**2
for i in range (len(nums)):
    print(square(nums[i]))

stringo='Hello, this is batman.'
last=lambda a:a[-1]
print(last(stringo))

evenSteven=lambda x:x%2==0
for i in range(len(nums)):
    print(evenSteven(nums[i]))

"""
Task 3 — map + filter
Using the list:

grades = [50, 65, 70, 85, 90, 30, 100]


Do:

Curve all grades by +5 using map

Extract passing grades (>= 60) using filter
"""
grades = [50, 65, 70, 85, 90, 30, 100]
improved_grades=list(map(lambda x:x+5,grades))
print(improved_grades)

passing_grades=filter(lambda x:x>=60,grades)
print(list(passing_grades))