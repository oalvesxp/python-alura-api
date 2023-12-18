from models.menu.eatery_menu import EateryMenu

class Dish(EateryMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description
    
    def __str__(self):
        return self._name
    
    def add_discount(self):
        self._price -= (self._price * 0.05)