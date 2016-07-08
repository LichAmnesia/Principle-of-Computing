# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-06-30 17:32:58
# @Last Modified time: 2016-06-30 17:53:40
# @FileName: BankAccount.py

class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.account = initial_balance        
        self.fee = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.account += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting 
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
        self.account -= amount
        if self.account < 0:
            self.fee += 5
            self.account -= 5

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.account

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee


def main():
    my_account = BankAccount(10)
    my_account.withdraw(15)
    my_account.deposit(20)
    print my_account.get_balance(), my_account.get_fees()
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


if __name__ == '__main__':
    main()