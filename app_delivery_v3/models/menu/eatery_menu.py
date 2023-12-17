from abc import ABC, abstractmethod

class EateryMenu:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @abstractmethod
    def add_discount(self):
        pass