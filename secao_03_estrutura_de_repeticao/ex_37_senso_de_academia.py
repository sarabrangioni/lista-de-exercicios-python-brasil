"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """ """
    cadastro = obter_input()
 
    resultado = descobre_mais_alto_e_baixo(cadastro)
    nome_do_mais_alto, mais_alto, nome_do_mais_baixo, mais_baixo = resultado
 
    resultado = descobre_mais_magro_gordo(cadastro)
    nome_do_mais_magro, mais_magro, nome_do_mais_gordo, mais_gordo = resultado
 
    media_altura, media_peso = descobrir_medias_de_altura_e_peso(cadastro)
 
    print(f"Cliente mais alto: {nome_do_mais_alto}, com {mais_alto} centímetros")
    print(f"Cliente mais baixo: {nome_do_mais_baixo}, com {mais_baixo} centímetros")
    print(f"Cliente mais magro: {nome_do_mais_magro}, com {mais_magro} kilos")
    print(f"Cliente mais gordo: {nome_do_mais_gordo}, com {mais_gordo} kilos")
    print("--------------------------------------------------")
    print(f"Media de altura dos clientes: {media_altura:.1f} centímetros")
    print(f"Media de peso dos clientes: {media_peso:.1f} kilos")
    print(f'Salário em 2018: R$ {salario:.2f}')
    aumento_percentual = 0.015
    for ano in range (2019,2024):
       salario = (salario * (1 + aumento_percentual))
       print(f'Salário em {ano}: R$ {salario:.2f}. Aumento porcentual: {(aumento_percentual * 100):.2f}%')
       aumento_percentual *= 2