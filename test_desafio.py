import pytest
from Funcionario import Funcionario
from FuncionarioComum import FuncionarioComum
from Gerente import Gerente
from SistemaRH import SistemaRH
from unittest.mock import patch


def test_funcionario_comum():
    funcionario = FuncionarioComum('Wendell', 1000)
    assert funcionario.calcular_bonus() == 100

def test_gerente():
    gerente = Gerente('Wendell Baresi', 2000,500)
    assert gerente.calcular_bonus() == 900.0


@patch("builtins.print")
def test_mostrar_bonus(mock_print):
    sistema = SistemaRH()
    funcionario = FuncionarioComum('Wendell', 1000)
    sistema.mostrar_bonus(funcionario)
    mock_print.assert_any_call('Registrando bonus do funcionario: Wendell')
    mock_print.assert_any_call('Nome: Wendell, Bonus: 100.0')