import sys

#account balance 
account_balance = float(500.25)

#defines the balance function that prints out the balance of user
def balance():
  print("Your current balance:\n %.2f" % account_balance)

#deposit function and print statement with placeholders for the amount
#takes input from user and adds it to the total 
def deposit():
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  balance = account_balance + deposit_amount
  print("Deposit was $%.2f, current balance is $%.2f" % (deposit_amount, balance))

  
#withdraw function 
#and if / else conditional statements along with printing the balance
#takes input from user and finds out if it is too high
#if that is the case it lets the user know
#if it isn't, gives user the withdrawal amount along with the current balance after the withdrawal
def withdraw():
  withdraw_amount = float(input("How much would you like to withdraw today?\n"))
  if withdraw_amount > account_balance:
    print("$%.2f is greater than your account balance of $%.2f" % (withdraw_amount, account_balance))
  else:
    balance = account_balance - withdraw_amount
    print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance))

#Prompt for user to take actian at the ATM
userchoice = input ("What would you like to do?\n")

#Conditional Statement that determines the input given by the user 
#D for deposit, W for withdrawl, B for balance and Q for quit
if (userchoice == 'D'):
    deposit ()
elif (userchoice == 'W'):
  withdraw ()
elif (userchoice == 'B'):
  balance ()
elif userchoice == 'Q':
  print("Thank you for banking with us.")
