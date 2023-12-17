class Eatery:
    base = []

    def __init__(self, name, category):
        '''Cria um objeto Restaurante e o adiciona à lista base.
        
        Input:
        - Nome
        - Categoria
        '''
        self.name = name
        self.category = category
        self.status = False
        Eatery.base.append(self)

    def __str__(self):
        return self.name
    
    def list_eatery():
        '''Lista todos os restaurantes cadastrados
        
        Output:
        - Nome
        - Categoria
        - Status
        '''
        for this in Eatery.base:
            print(f'{this.name} | {this.category} | {this.status}')


box_mineito = Eatery('Box Mineiro', 'Caseiro')
box_mineito = Eatery('La Carbonara', 'Italiano')

Eatery.list_eatery()