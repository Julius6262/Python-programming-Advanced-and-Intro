class BankAccount:
    def __init__(self, owner: str, ac_num: str, balance: float):
        self._owner = owner
        self._ac_num = ac_num
        self._balance = balance
        

    def deposit(self, amount: float):
        
        self._balance += amount
        self.__service_charge()
        

    def withdraw(self, amount: float):
        if self._balance > amount:
            
            self._balance -= amount
            self.__service_charge()
            
        else:
            raise ValueError("Not enough money")

    @property
    def balance(self):
        return self._balance

    def __service_charge(self):
        service_charge = self._balance * 0.01
        self._balance -= service_charge

