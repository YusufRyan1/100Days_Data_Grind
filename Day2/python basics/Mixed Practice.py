"""
Q1: Frequency counter

Given a sentence, count how many times each word appears.
"""
# sentence="Today the weather is nice and today I feel nice because the weather makes me feel happy today"
# list1=sentence.split()
# # print(list1)
# randomdict={}
# for word in list1:
#     counter=0
#     for word2 in list1:
#         if word.lower()==word2.lower():
#             counter+=1
#     if(word not in randomdict):
#         randomdict.update({word:counter})
# print(randomdict)


"""
🔹 Q2: Find students who passed

Input:

students = {"Ryan": 90, "Ahmed": 50, "Sara": 76, "Mona": 30}


Print only students with score > 60.
"""
# students = {"Ryan": 90, "Ahmed": 50, "Sara": 76, "Mona": 30}
# passed_students=[]
# for key,value in students.items():
#     if value>60:
#         passed_students.append(key)
# print(passed_students)


"""
🔹 Q3: Unique names

Given this list:

names = ["Ali", "Ali", "Omar", "Sara", "Omar"]


Get unique names (with sets).
"""
# names = ["Ali", "Ali", "Omar", "Sara", "Omar"]
# unique_names=set(names)
# print(unique_names)

'''
🔹 Q4: Highest score

Return the student with the highest score.
'''
students = {"Ryan": 90, "Ahmed": 50, "Sara": 76, "Mona": 30}
owner=''
max=0
for key,value in students.items():
    if value>max:
        max=value
        owner=key
print(owner)
