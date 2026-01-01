'''  
Problem:

A bank allows withdrawal only if balance ≥ amount

If not, raise a custom exception
'''

# Creating a custom exception

class InsufficientBalance(Exception):
     pass


# creating a function to withdraw money

def withdrawAmount(balance,amount):
     if(balance < amount):
          raise InsufficientBalance("Insufficient Balance to withdraw")
     else:
          balance -= amount
          print("Your remaining balance -> ", balance)


try:
     withdrawAmount(7000,5000)
     withdrawAmount(5000,7000)
except InsufficientBalance as e:
     print("Error -> ",e)
else:
     print("Withdrawal Successful")
finally:
     print("Process Done -> Thank you")