def main():
    text = input("Input: ")
    print("Output: " + convert(text))


def convert(text):
    result = ""
    for c in text:
        if c.lower() in  ["a", "e", "i", "o", "u"]:
            continue
        else:
            result += c
    return result

main()
            