class Account:

    def __init__(self, name: str) -> None:
        """
        Function to set up account object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0
    def deposit(self, amount) -> bool:
        """
        If else function to determine if a correct deposit is made and is added to account balance
        :param amount: account balance added
        :return: bool value
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False
    def withdraw(self, amount) -> bool:
        """
        if else function to determine if a correct withdrawal can be made without making account balance negative
        :param amount: account balance subtracted
        :return: bool value
        """
        if amount > 0:
            if amount < self.__account_balance:
                self.__account_balance = self.__account_balance - amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        """
        function to return total account balance that may have been changed by deposit or withdrawal
        :return: total account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        function to return the name on the account
        :return: name of account
        """
        return self.__account_name
