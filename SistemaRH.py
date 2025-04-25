
class SistemaRH:
    def mostrar_bonus(self, Funcionario):
        print(f"Nome: ", Funcionario.get_nome(), "Bonus: ", Funcionario.calcular_bonus())