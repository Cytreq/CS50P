# get input 
# check is this 42 or other cases 
# if it's correct print yes otherwise print no

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    if answer == "42" or answer == "forty two" or answer == "forty-two" :
        print("Yes")
    else:
        print("No")

main()
