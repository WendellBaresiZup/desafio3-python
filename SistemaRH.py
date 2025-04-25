class SistemaRH:

    def logar_acao(func):
        def nova_funcaro(Funcionario):
            print(f"Registrando bonus para um novo funcionario: {Funcionario.get_nome()}")
            return func(Funcionario)

    @logar_acao
    def mostrar_bonus(self, Funcionario):
        print(f"Nome: {Funcionario.get_nome()}, Bonus: {Funcionario.calcular_bonus()}")