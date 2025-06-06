# Sistema de Funcionários de uma Zup Up
Bem-vindo ao Sistema de Funcionários de uma Startup! Este projeto implementa um sistema para cálculo de bônus dos funcionários de uma startup, utilizando conceitos de Programação Orientada a Objetos (POO) e testes automatizados com pytest. O sistema suporta dois tipos de funcionários: comuns e gerentes.

![Image](https://github.com/user-attachments/assets/ec34325d-16f2-4950-9e2e-d1a8fbf1de28)

## Descrição do Desafio

### O objetivo do sistema é:

* Calcular o bônus dos funcionários com base em suas categorias (comum ou gerente).
* Registrar ações relacionadas ao cálculo de bônus por meio de um decorator de log.
* Garantir a correção dos cálculos e validações através de testes automatizados .

## Exemplo de Uso
* Cadastrar Funcionário e Exibir Bônus

## Criando funcionários
* funcionario_comum = FuncionarioComum("Alice", 3000)
* gerente = Gerente("Bob", 5000, 1000)

## Exibindo bônus
* sistema.mostrar_bonus(funcionario_comum)
* sistema.mostrar_bonus(gerente)
- Saída Esperada
* Registrando bônus para um novo funcionário: Alice
* Nome: Alice, Bônus: 300.0
* Registrando bônus para um novo funcionário: Bob
* Nome: Bob, Bônus: 2000.0

## Como Executar os Testes
##### Certifique-se de que o pytest está instalado:
```bash
pip install pytest
```

##### Execute os testes:
```bash
pytest -v test_nomedoteste.py
```

Licença
Este projeto foi desenvolvido como parte de um desafio de aprendizado. Sinta-se livre para utilizá-lo e aprimorá-lo! 🚀
