# 1.1 Implement a recursive function to calculate the factorial of a given number
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))

# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

year = 2023

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

#2.1 ''Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance. Include methods to
deposit money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:
  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      # self._account_balance = self._account_balance+amount
      print("Deposited {}. New balance: {}".format(amount,
                                                     self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      # self._account_balance = self._account_balance - amount
      print("Withdrew {}. New balance: {}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account #{}): {}".format(
        self._account_holder_name, self._account_number,
        self.__account_balance))
# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="Hari Prabu",
                      initial_balance=5000.0)
# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()

#2.2 Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
# Define the Player class
class Player:
    def play(self):
        print("The player is playing cricket.")
# Define the Batsman class, derived from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
# Define the Bowler class, derived from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
# Create objects of Batsman and Bowle
