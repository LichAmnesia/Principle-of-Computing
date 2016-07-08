1. Enter the type of the Python expression 3.14159 below. Remember that capitalization is important.
 - Float

2. An if statement can have how many elif parts?
 - Unlimited, i.e., 0 or more

3. Consider the following Python code snippet:
 def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60
print (clock_helper(90))

- None

4. In Python, what character always appears at the end of the line before the start of an indented block of code?
- :

5. Which of the following expressions returns the last character in the non-empty string my_string?

- my_string[len(my_string) - 1]

6. What is the primary difference between a list and a tuple?
- Lists are mutable. Tuples are immutable.

7. Consider the following snippet of Python code. What is the value of val2[1] after executing this code?

val1 = [1, 2, 3]
val2 = val1[1:]
val1[2]  = 4
#print val2[1]

- 3

8. Which of the following Python expressions is a valid key in a Python dictionary?
- False, "", 0

9. 

def appendsums(lst):
    sum = 0
    for i in range(25):
        sum = lst[len(lst) -1] + lst[len(lst) -2] + lst[len(lst) -3]
        #print sum
        lst.append(sum)
    return lst

sum_three = [0, 1, 2]
appendsums(sum_three)
#print sum_three[10]
print sum_three[20]

- 101902

10. 

class BankAccount:
    balance = 0
    fee = 0
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        if self.balance - amount < 0:
            self.balance = self.balance - amount -5
            self.fee = self.fee + 5
        else:
            self.balance = self.balance - amount
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()

- -60 75

