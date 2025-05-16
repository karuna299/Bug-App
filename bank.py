def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

