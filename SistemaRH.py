class SistemaRH:

    @staticmethod
    def logar_acao(func):
        def nova_funcao(self, Funcionario, *args, **kwargs):
            print(f"Registrando bonus do funcionario: {Funcionario.get_nome()}")
            return func(self,Funcionario, *args, **kwargs)
        return nova_funcao

    @logar_acao
    def mostrar_bonus(self, Funcionario):
        print(f"Nome: {Funcionario.get_nome()}, Bonus: {Funcionario.calcular_bonus()}")