import random  

MIN_BET = 1
MAX_BET = 100

COLS = 3

symbols = { # In each wheel
    "A": 5,
    "B": 5,
    "C": 5,
    "D": 5
}

def get_slot_machine_spin(cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = [0] * cols
    for col in range(len(columns)):
            value = random.choice(all_symbols)
            columns[col] = value
            all_symbols.remove(value)
    return columns
    


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def betAmount():
    while True :
        betAmount = input("What would you like to bet? $")
        if betAmount.isdigit():
            betAmount = int(betAmount)
            if betAmount > 0 and betAmount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return betAmount
def validBet(balance, bet):
    if bet <= balance:
        return True
    else:
        return False
    
def main():
    continuePlay = 'Y'
    balance = deposit()
    while balance and continuePlay == 'Y':
        while True:
            bet = betAmount()
            if validBet(balance, bet):
                break
            else:
                print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        print(f"You are betting ${bet}.")
        slot_spin = get_slot_machine_spin(3, symbols)
        print(slot_spin)
        if len(set(slot_spin)) == 1:
            balance += bet
            print(f"You won! Your balance is now ${balance}")
        else:
            balance -= bet
            print(f"You lost! Your balance is now ${balance}")
        if balance > 0:
            continuePlay = input("Would you like to play again? Y/N ")

    if balance <= 0:    
        print("You ran out of balance.")
    elif continuePlay == 'N':
        print("Thanks! Have a good day")

main()