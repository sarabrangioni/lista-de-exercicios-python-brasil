"""
Exercício 16 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
 valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
 demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário.

Mostrar raízes com uma casa decimal.

    >>> resolver_equacao_do_segundo_grau(0, 3, 4)
    'Valor do coeficiente a deve ser diferente de 0'
    >>> resolver_equacao_do_segundo_grau(2, 1, 2)
    'Delta negativo (-15), por isso não existem raízes reais'
    >>> resolver_equacao_do_segundo_grau(1, 2, 1)
    'Delta é 0, raíz única no valor de -1.0'
    >>> resolver_equacao_do_segundo_grau(1, 4, 3)
    'Delta é 4, raízes são -1.0 e -3.0'

"""


def resolver_equacao_do_segundo_grau(a: float, b: float, c: float):
    """Escreva aqui em baixo a sua solução"""
    import math
    if a==0:
        print("'Valor do coeficiente a deve ser diferente de 0'")
    else:
        delta= b*b - (4*a*c)
        if delta<0:
            print(f"'Delta negativo ({delta:.0f}), por isso não existem raízes reais'")
        elif delta == 0:
            raiz = -b / (2*a)
            print (f"'Delta é {delta:.0f}, raíz única no valor de {raiz:.1f}'")
        else:
            raiz1 = (-b + math.sqrt(delta) ) / (2*a)
            raiz2 = (-b - math.sqrt(delta) ) / (2*a)
            print(f"'Delta é {delta:.0f}, raízes são {raiz1:.1f} e {raiz2:.1f}'")
