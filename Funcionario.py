from abc import ABC, abstractmethod

class Funcionario():
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("O salario nao pode ser nulo!")
        self.__salario = salario