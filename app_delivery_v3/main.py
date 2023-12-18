from models.restaurant import Eatery
from models.menu.drink import Drink
from models.menu.dish import Dish

pizza = Eatery('Pizza Hut', 'Pizzaria')

juice = Drink('Água com gás', 2.50, '350 ml')
juice.add_discount()

plate = Dish('Broto de Peperoni', 3.50, 'Pizza pequena de 4 pedaços')
plate.add_discount()

pizza.add_menu(juice)
pizza.add_menu(plate)

def main():
    pizza.show_menu

if __name__ == '__main__':
    main()