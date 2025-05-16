#BEFORE FIXING THE BUG ---
#def withdraw(amount, balance):
    #return balance - amount  # ❌ Bug: No check for negative balance!

#After fixing the bug ---
 def withdraw(amount, balance):
     if amount > balance:
         raise ValueError("Insufficient funds!")  # ✅ Prevents negative balance
     return balance - amount
