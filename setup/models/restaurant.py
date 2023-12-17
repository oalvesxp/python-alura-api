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
        print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}")
        for this in cls.base:
            print(f'{this._name.ljust(20)} | {this.category.ljust(20)} | {this.status}')

    @property
    def status(self):
        '''Altera o output do status do objeto.'''
        return '☑' if self._status else '☐'
    
    def update_status(self):
        '''Altera o valor do status do objeto.'''
        self._status = not self._status
