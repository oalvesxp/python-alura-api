from models.menu.eatery_menu import EateryMenu

class Drink(EateryMenu):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    
    def __str__(self):
        return self._name
    
    def add_discount(self):
        self._price -= (self._price * 0.08)