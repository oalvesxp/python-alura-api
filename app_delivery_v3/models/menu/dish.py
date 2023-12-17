from models.menu.eatery_menu import EateryMenu

class Dish(EateryMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description