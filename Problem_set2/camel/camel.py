def main():
    camel = input("Camel case: ")
    print(convert(camel))


def convert(text):
    result = ""
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char 
    return result

main()