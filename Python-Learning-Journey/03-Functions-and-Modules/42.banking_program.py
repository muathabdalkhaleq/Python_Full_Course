# Banking program 

def show_balance(balance):
    print("********************")
    print(f"your balance is ${balance:.2f}")
    print("********************")

def deposite():
    print("********************")
    amount = float(input("Enter an amount to be deposit"))
    print("********************")
    if amount < 0 :
        print("********************")
        print("That's not valid amount")
        print("********************")
        return 0 
    else:
        return amount
def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn"))
    print("********************")
    
    if amount > balance:
        print("********************")
        print("Insufficient funds")
        print("********************")
        return 0 
    elif amount <0:
        print("********************")
        print("Amount must be grater than 0")
        print("********************")
        return 0
    else:
        return amount
def main():

    balance = 0 
    is_running = True

    while is_running:
        print("********************")
        print("  Banking Program")
        print("********************")
        print("Bankig program")
        print("Show Balance")
        print("Deposit")
        print("Withdraw")
        print("Exit")
        print("********************")
        choise = input("Enter your choise ?(1 - 4): ")
        print("********************")

        if choise == '1':
            show_balance(balance)
        elif choise == '2':
            balance += deposite()
        elif choise == '3':
            balance -= withdraw(balance)
        elif choise == '4':
            is_running = False
        else:
            print("********************")
            print("That is not valid choise")
            print("********************")

    print("********************")
    print("thank you ! have a nice day !")
    print("********************")
    

if __name__ == '__main__':
    main()