from models.rating import Rating
from models.menu.eatery_menu import EateryMenu

class Eatery:
    base = []

    def __init__(self, name, category):
        '''Cria um objeto Restaurante e o adiciona à lista base.
        
        Input:
        - Nome
        - Categoria
        '''
        self._name = name.title()
        self.category = category
        self._status = False
        self._rating = []
        self._menu = []
        Eatery.base.append(self)

    def __str__(self):
        return self._name
    
    @classmethod
    def list_eatery(cls):
        '''Lista todos os restaurantes cadastrados
        
        Output:
        - Nome
        - Categoria
        - Status
        '''
        print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        for this in cls.base:
            print(f'{this._name.ljust(20)} | {this.category.ljust(20)} | {str(this.rating_avg).ljust(20)} | {this.status}')

    @property
    def status(self):
        '''Altera o output do status do objeto.'''
        return '☑' if self._status else '☐'
    
    def update_status(self):
        '''Altera o valor do status do objeto.'''
        self._status = not self._status
    
    def get_rating(self, customer, grade):
        '''Adiciona as avaliações a lista de avaliações dentro do objeto Eatery'''
        if 0 < grade <= 5:
            this = Rating(customer, grade)
            self._rating.append(this)
    
    @property
    def rating_avg(self):
        '''Calcula o valor da nota média que o restaurante recebeu
        
        Output:
        - Nota média
        '''
        if not self._rating:
            return '-'
        
        total_grade = sum(this._grade for this in self._rating)
        count_grade = len(self._rating)
        average = round(total_grade / count_grade, 1)
        
        return average

    def add_menu(self, value):
        if isinstance(value, EateryMenu):
            self._menu.append(value)
    
    @property
    def show_menu(self):
        print(f'Cardápio do restaurante {self._name}\n')
        
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, 'description'):
                dish_message = f'{i}. Nome: {item._name.ljust(20)} | Preço: R${str(item._price).ljust(20)} | Descrição: {item.description}'
                print(dish_message)
            else:
                drink_message = f'{i}. Nome: {item._name.ljust(20)} | Preço: R${str(item._price).ljust(20)} | Tamanho: {item.size}'
                print(drink_message)
