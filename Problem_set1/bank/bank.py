# get input from a user 
# if user type hello you print 0$ if user greeted with greeting starting with h print 0$
# in other cases print 100$

def main():
    greeting = input("Greeting: ").lower()
    if greeting.startswith("hello" or "Hello"):
        print("0$")
    elif "h" in greeting:
        print("20$")
    else:
        print("100$")
main()