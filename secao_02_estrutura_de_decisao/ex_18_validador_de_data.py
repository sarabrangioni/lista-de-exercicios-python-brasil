"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

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

        elif mes== 2 and dia >0 and dia <=29:
          print("'Data válida'")

        elif mes== 3 and dia >0 and dia <32:
          print("'Data válida'")

        elif mes==4 and dia >0 and dia <31:
          print("'Data válida'")

        elif mes==5 and dia > 0 and dia <32:
          print("'Data válida'")

        elif mes==6 and dia > 0 and dia <31:
          print("'Data válida'")

        elif mes==7 and dia > 0 and dia <32:
          print("'Data válida'")

        elif mes== 8 and dia > 0 and dia <31:
          print("'Data válida'")

        elif mes==9 and dia > 0 and dia <31:
          print("'Data válida'")

        elif mes== 10 and dia >0 and dia <32:
          print("'Data válida'")

        elif mes == 11 and dia > 0 and dia < 31:
          print("'Data válida'")

        elif mes == 12 and dia> 0 and dia <32:
          print("'Data válida'")
        else:
          print("'Data inválida'")
    else:
      print("'Data inválida'")
