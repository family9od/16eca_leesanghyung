balance_won = 0

def deposit(amount):
    global balance_won
    balance_won += int(amount)

def pay(amount):
    global balance_won
    balance_won -= int(amount)

def check():
    global balance_won
    return balance_won