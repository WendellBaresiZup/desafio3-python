from Funcionario import Funcionario


class FuncionarioComum(Funcionario):

    def calcular_bonus(self):
        return self.get_salario() * 0.1