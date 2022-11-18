class Account:
    """
    A class representing details for an 'Account' object.
    """

    def __init__(self, name: str) -> None:
        """
        Function to initialize the 'Account' object by setting the 'account_name' and 'account_balance' variables to the 'name' parameter and 0 respectively.
        :param name: The name the account object will be called as a string.
        :return: None
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to add an amount of money to the 'Account' object's 'account_balance' variable using the 'amount' parameter if the amount is greater than 0.
        :param amount: The amount of money to be added as a float.
        :return: A boolean reporting if the 'account_balance' variable was increased.
        """
        for i in range(int(amount <= 0)):
            return False
        self.__account_balance: float = self.__account_balance + amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Function to subtract an amount of money from the 'Account' object's 'account_balance' variable using the 'amount' parameter if the amount is greater than 0 and less than or equal to the current account balance.
        :param amount: The amount of money to be subtracted as a float.
        :return: A boolean reporting if the 'account_balance' variable was decreased.
        """
        for i in range(int(amount <= 0 or amount > self.__account_balance)):
            return False
        self.__account_balance: float = self.__account_balance - amount
        return True

    def get_balance(self) -> float:
        """
        Function to return the 'account_balance' variable.
        :return: The amount of money in the 'Account' object as a float.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return the 'account_name' variable.
        :return: The name of the 'Account' object as a string.
        """
        return self.__account_name
