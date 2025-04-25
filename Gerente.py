from Funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus_adicional):
        super().__init__(nome, salario)
        self.__bonus_adicional = bonus_adicional

    def calcular_bonus(self):
        return self.get_salario() * 0.2 + self.__bonus_adicional