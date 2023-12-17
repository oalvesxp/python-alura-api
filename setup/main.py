from models.restaurant import Eatery

mexican = Eatery('Mexicaníssimo', 'Mexicano')
pizza = Eatery('Pizza Hut', 'Pizzaria')
japanese = Eatery('Nombei Izakaya', 'Japonesa')

japanese.update_status()

def main():
    Eatery.list_eatery()

if __name__ == '__main__':
    main()