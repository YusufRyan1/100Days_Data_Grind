# 1.Create a dictionary for a student with name, age, score.
student={"name":"Yusuf","age":24,"score":97.68}

# 2.Update the score.
student.update({"score":95})

# 3.Add a new key "passed" (True/False).
student['passed']=True
print(student)

# 4.Loop through keys.
for key in student:
    print(key)

# 5.Loop through values.
for value in student.values():
    print (value)

# 6.Loop through items.
for item in student.items():
    print(item)

# 7.Delete a key
student.pop('passed')


# 8.Check if a key exists.
print(student.get('passed','not found'))

# 9.Create a dict of students → scores and print the highest score.
students_scores = {
    "Yusuf": 88,
    "Mariam": 92,
    "Omar": 76,
    "Sarah": 95,
    "Khaled": 81,
    "Amira": 99,
    "Hassan": 67,
    "Lina": 73,
    "Ahmed": 90,
    "Rana": 84,
}
max=0
owner=""
for key,value in students_scores.items():
    if(value>max):
        max=value
        owner=key
print(f"{owner} had scored {max}")

# .10 Nested dict:students = {"A": {"math": 80}, "B": {"math": 90}} Get student B’s math score.
students = {"A": {"math": 80}, "B": {"math": 90}}
print(students["B"]['math'])


