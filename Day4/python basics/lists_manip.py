#Itterators (enumerate,reversed,zip,map,filter)
letters=['a','b','c']

# enumerate(itterable) returns index , value
# for index,value in enumerate(letters):
#     print(value,index)
# nums=[1,2,3]
# ZIP(itterable,itterable) returns tubles of pairs
# new=list(zip(letters,nums))
# for l,n in zip(letters,nums):
#     print(l,n)
# Reversed
# reversed_letters=list(reversed(letters))
# print(reversed_letters)

# Map (function,itterable)

# print(list(map(str.upper,reversed(letters))))
# names=[' Maria ','John ', ' Kumar']
# cleaned_names=list(map(str.strip,names))
# print(cleaned_names)
# string_nums=['1','2','3']
# integers=list(map(int,string_nums))
# print(integers)
# for num in integers:
#     print(type(num))

# Filter(Rule,itterable)
# letters=['a','','b',False,'c',None]
# filtered_letters=list(filter(None,letters))
# print(filtered_letters)
# items=['sql','123','Python','22']
# only_alpha=list(filter(str.isalpha,items))
# print(only_alpha)

##lambda

# multiplay=lambda x:x*2
# print(multiplay(2))

# addition=lambda x,y:x+y
# print(addition(4,5))
# prices=['$12.50','$9.99','$100']
# prices_float=list(map(lambda p:float(p.replace('$','')),prices))
# print(sum(prices_float))
# prices=[120,30,300,80]

# filtered_prices=list(filter(lambda p:p>100,prices))
# print(filtered_prices)

# students=[['Maria',85],
#           ['Kumar',90],
#           ['Max',60]
#           ]
# filtered_students=list(filter(lambda row:row[1]>70,students))
# print(filtered_students)
# students=[['Maria',85],
#           ['Kumar',90],
#           ['Max',60]]

# print(students[0][0].lower().startswith('m'))
# filtered=list(filter(lambda row:row[0].lower().startswith('m'),students))
# print(filtered)

## List comprehensions  

domain=['www.google.com','openai.com','localhost','WWW.DATAWITHBARAA.com']
cleaned=[
    d.lower().replace('www.','')
    for d in domain
    if '.' in d
]
print(cleaned)