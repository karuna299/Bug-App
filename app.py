from bank import withdraw

# Initial balance
balance = 1000  

# Simulate withdrawal
try:
    print(f"Current balance: ${balance}")
    amount = 205  # Trying to withdraw more than balance
    print(f"Withdrawing ${amount}...")
    balance = withdraw(amount, balance)
    print(f"New balance: ${balance}")
except ValueError as e:
    print(f"Error: {e}")
