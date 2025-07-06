def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("Breakfast time")
    elif 12 <= t <= 13:
        print("Lunch time")
    elif 18 <= t <= 19:
        print("Dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
   
    time = hours + minutes / 60
    return time



if __name__ == "__main__":
    main()