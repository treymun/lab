class Account:

    def __init__(self, name: str) -> None:
        """
        Function to set up account object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0
    def deposit(self, amount) -> bool:
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False
    def withdraw(self, amount) -> bool:
        if amount > 0:
            if amount < self.__account_balance:
                self.__account_balance = self.__account_balance - amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
