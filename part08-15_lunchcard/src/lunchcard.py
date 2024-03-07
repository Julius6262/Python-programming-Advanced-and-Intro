
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, amount: int):
        if amount > 0:
            self.balance += amount
        else: raise ValueError("You cannot deposit an amount of money less than zero")
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
############################################################################################


lunch_card_peter = LunchCard(20)
lunch_card_grace = LunchCard(30)
lunch_card_peter.eat_special()
lunch_card_grace.eat_lunch()
print(f"Peter: {lunch_card_peter}")
print(f"Grace: {lunch_card_grace}")
lunch_card_peter.deposit_money(20)
lunch_card_grace.eat_special()
print(f"Peter: {lunch_card_peter}")
print(f"Grace: {lunch_card_grace}")
lunch_card_peter.eat_lunch()
lunch_card_peter.eat_lunch()
lunch_card_grace.deposit_money(50)
print(f"Peter: {lunch_card_peter}")
print(f"Grace: {lunch_card_grace}")