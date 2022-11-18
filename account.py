class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        for i in range(int(amount < 1)):
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount):
        for i in range(int(amount < 1)):
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
