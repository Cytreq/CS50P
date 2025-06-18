variable = input() #ask user for iput

# converting to emojis
def convert(variable):
    text_sad =  variable.replace(":(", "🙁")
    text_happy = variable.replace(":)", "🙂")
    return text_sad, text_happy
    
#main part of the program
def main():
    text_sad, text_happy = convert(variable)
    converted_text = convert(variable)

    if "hello :)" in variable and "goodbye :(" in variable: 
        print(converted_text)
   
    elif "hello :)" in variable:
        print(text_happy)

    elif "goodbye :(" in variable:
        print(text_sad)



main()


### """ I have to clean this code a litlle bit 
#   fix the bug with "hello :) goodbye :( because I'm getting wrong input in this case""""



