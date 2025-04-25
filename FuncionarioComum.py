from Funcionario import Funcionario


class FuncionarioComum(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.get_salario() * 0.1