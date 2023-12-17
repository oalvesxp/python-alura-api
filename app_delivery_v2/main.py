from models.restaurant import Eatery

mexican = Eatery('Mexicaníssimo', 'Mexicano')
pizza = Eatery('Pizza Hut', 'Pizzaria')
japanese = Eatery('Nombei Izakaya', 'Japonesa')

japanese.update_status()
japanese.get_rating('Gui', 10)
japanese.get_rating('Fabio', 7.5)
japanese.get_rating('Nica', 7)
japanese.get_rating('Junior', 5.5)
japanese.get_rating('Junior', 3.5)

pizza.update_status()
pizza.get_rating('Joao', 8)
pizza.get_rating('Maria', 5)

def main():
    Eatery.list_eatery()

if __name__ == '__main__':
    main()