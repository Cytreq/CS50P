def main():
    ammount_due = 50
    ammount_due = int(ammount_due)
    while ammount_due > 0:
        print(f"Ammount due: {ammount_due}")
        
        coin = check_coin()
        if coin == 0:
            continue
        elif coin > ammount_due:
            continue
        ammount_due -= coin
    print("Change owed: 0")



def check_coin():
    inserted_coin = int(input("Inserted coin: "))
    if inserted_coin in [5, 10, 25]:
        return inserted_coin
    else: 
        return 0
    
main()
