
def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    match y:    
        case y if y == "+":
            result = x + z 
        case y if y == "-":
            result = x - z 
        case y if y == "*":
            result = x * z 
        case y if y == "/" and not z == 0:
            result = x / z
        case y if y == "/" and z == 0:
            print("You cannot divide by 0 ")
            return
        case _:
            print("Error")
    result = round(result, 1)
    print(result)
main()
    




