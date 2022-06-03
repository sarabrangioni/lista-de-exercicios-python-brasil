"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    if x > y and x > z and y < z:
        print ("Maior: ", x)
        print ("Menor: ", y)
    elif y > x  and y > z and z < x:
        print ("Maior: ", y)
        print ("Menor: ", z)
    elif z > x and z > y and x < y: 
        print ("Maior: ", z)
        print ("Menor: ", x)