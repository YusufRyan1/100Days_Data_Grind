x=int(input("please enter the first number: "))
y=int(input("please enter the second number: "))
z=input("please enter the arithmetic operator: ")
if(z=="+"):
    print(x+y)
elif(z=="*"):
    print(x*y)
elif(z=="-"):
    print(x-y)
elif(z=="/"):
    print(x/y)
else:
    print("Unknown operator")