"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""
def validar_data(data: str):
    """Escreva aqui em baixo a sua soluçãodia = int(data[0:2])"""
    data_splitada = (data.split('/'))
    if len(data_splitada) == 3:
        dia = int(data_splitada[0])
        mes = int(data_splitada[1])
        ano = int(data_splitada[2])
        if mes== 1 and dia >0 and dia < 32:
          print("'Data válida'")
            #feve
        elif mes== 2 and dia >0 and dia <=29:
          print("'Data válida'")
            #mar
        elif mes== 3 and dia >0 and dia <32:
          print("'Data válida'")
            #abr
        elif mes==4 and dia >0 and dia <31:
          print("'Data válida'")
            #mai
        elif mes==5 and dia > 0 and dia <32:
          print("'Data válida'")
            #jun
        elif mes==6 and dia > 0 and dia <31:
          print("'Data válida'")
            #jul
        elif mes==7 and dia > 0 and dia <32:
          print("'Data válida'")
            #ago
        elif mes== 8 and dia > 0 and dia <31:
          print("'Data válida'")
            #set
        elif mes==9 and dia > 0 and dia <31:
          print("'Data válida'")
            #out
        elif mes== 10 and dia >0 and dia <32:
          print("'Data válida'")
            #nov
        elif mes == 11 and dia > 0 and dia < 31:
          print("'Data válida'")
            #dez
        elif mes == 12 and dia> 0 and dia <32:
          print("'Data válida'")
        else:
          print("'Data inválida'")
    else:
      print("'Data inválida'")
