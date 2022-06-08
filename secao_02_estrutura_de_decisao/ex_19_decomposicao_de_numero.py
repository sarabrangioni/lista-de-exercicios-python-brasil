"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


from math import floor


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""

    resto_c= numero % 100
    resto_dez= resto_c % 10
    uni= int(resto_dez / 1)

    dez= int(numero /10)
    cen = int(numero/100)
    dezena = int(floor((numero % 100) /10))
## Unidades
    if numero < 10:
        if numero == 1 :
            print (f"'{numero} = {uni} unidade'")
        elif numero < 0:
            print("'O número precisa ser positivo'")
        else:
            print (f"'{numero} = {uni} unidades'")
#####################################################

## Dezenas
    if numero >= 10 and numero <= 99:
        if uni==0 and dez > 1:
            print(f"'{numero} = {dez} dezenas'")
        elif uni==0:
            print(f"'{numero} = {dez} dezena'")
        elif uni==1:
            print(f"'{numero} = {dez} dezenas e {uni} unidade'")
        elif dez ==1:
            print(f"'{numero} = {dez} dezena e {uni} unidades'")
        else:
            print(f"'{numero} = {dez} dezenas e {uni} unidades'")
####################################################

## Centenas
    if numero >= 100:
                    #1000
        if numero >999:
            print(f"'O número precisa ser menor que 1000'")
        elif cen > 1 and dezena >1 and uni > 1:
         print(f"'{numero} = {cen} centenas, {dezena} dezenas e {uni} unidades'")
        elif cen==1 and dezena == 0 and uni == 0:
            print(f"'{numero} = {cen} centena'")
        elif cen>1 and dezena == 0 and uni == 0:
            print(f"'{numero} = {cen} centenas'")
        elif cen>1 and dezena==0 and uni>1:
            print(f"'{numero} = {cen} centenas e {uni} unidades'")
        elif cen>1 and dezena > 1 and uni == 0:
            print(f"'{numero} = {cen} centenas e {dezena} dezenas'")
        elif cen >1 and dezena == 1 and uni ==0 :
            print(f"'{numero} = {cen} centenas e {dezena} dezena'")
        elif cen > 1 and dezena == 0 and uni ==1:
            print(f"'{numero} = {cen} centenas e {uni} unidade'")
        elif cen== 1 and dezena == 0 and uni == 1:
            print(f"'{numero} = {cen} centena e {uni} unidade'")
        elif cen > 1 and dezena == 1 and uni == 1:
            print(f"'{numero} = {cen} centenas, {dezena} dezena e {uni} unidade'")
        elif cen == 1 and dezena == 1 and uni == 1:
            print(f"'{numero} = {cen} centena, {dezena} dezena e {uni} unidade'")