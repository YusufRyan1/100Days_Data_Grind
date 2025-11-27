def greetings(greeting = 'Hello'):
    return greeting


print(greetings("hey dude"))

def students(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['math', 'programming', 'history']
info={'name': 'yusuf', 'age': 24}

students(*courses,**info)