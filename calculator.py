x = input("What's your first number? ")
y = input("What's your second number? ")

operation = input("""What operation do you want to do? Chose one from the list: 
1: + 
2: -
3: * 
 4: / 
""")
operation = int(operation)
x = float(x)
y = float(y)

if operation == 1:
    print(x + y)
elif operation == 2:
    print(x - y )
elif operation == 3:
    print(x * y)
elif operation == 4: 
    if y == 0:
        print("Don't division by 0")
    else:
        print(x / y )
else:
    print("Invalid operation!")