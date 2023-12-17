class Restaurant:
    def __init__(self, name, category):
        '''Cria um objeto Restaurante.
        
        Input:
        - Nome
        - Categoria
        '''
        self.name = name
        self.category = category
        self.status = False

    def __str__(self):
        return self.name


box_mineito = Restaurant('Box Mineiro', 'Caseiro')
print(box_mineito)