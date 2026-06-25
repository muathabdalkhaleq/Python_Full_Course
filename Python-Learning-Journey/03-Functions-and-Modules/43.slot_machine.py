
import random

def spin_row():
    symbols=['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("👀   👀   👀   👀   ")
    print("  |  ".join(row))
    print("👀   👀   👀   👀   ")

def get_payout(row,bet):
    if row [0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 4
        if row[0] == '🍋':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐':
            return bet * 20

    return 0
def main():
    balance = 100
    print("********************************")
    print("     welcome to Python slots    \n")
    print("     Symbols : 🍒  🍉 🍋 🔔 ⭐\n")
    print("********************************")
    while balance > 0 :
        print(f"current balance is ${balance:.2f}")

        bet = input("place a bet value:")
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("insufficient funds")
            continue
        if bet <= 0 :
            print("bet must be grater than 0")
            continue
        balance -= bet
        row = spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0 :
            print(f"You Win ${payout:.2f} 👏")
        else:
            print("sorry you lost this round😭")
        
        balance += payout

        play_again = input("            😍  Do you want to spin again?    😍  : (Y,N)").upper()
        if play_again != 'Y':
            break

    print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
    print(f"    😁 Your Final Balance IS {balance:.2f} 😁")
    print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")

    

if __name__ == '__main__':
    main()
