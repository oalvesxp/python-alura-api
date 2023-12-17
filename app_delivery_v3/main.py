from models.restaurant import Eatery
from models.menu.drink import Drink
from models.menu.dish import Dish

pizza = Eatery('Pizza Hut', 'Pizzaria')

juice = Drink('Água com gás', 2.50, '350 ml')
plate = Dish('Broto de Peperoni', 3.50, 'Pizza pequena de 4 pedaços')

pizza.add_menu(juice)
pizza.add_menu(plate)

def main():
    print(juice)
    print(plate)

if __name__ == '__main__':
    main()