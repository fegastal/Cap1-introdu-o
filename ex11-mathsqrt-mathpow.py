'''Exercício 11

Escreva um programa para resolver o problema de determinar o período orbital de qualquer corpo que orbita
em volta de qualquer estrela. Vamos escolher a Gliese 581 (wikipedia.org/wiki/Gliese_581)
'''

import math

m1 = float(input("Digite o valor da massa do primeiro objeto no espaço:\n"))
m2 = float(input("Digite o valor da massa do segundo objeto no espaço:\n"))
a = float(input("Digite o valor do raio médio entre ambos:\n"))

p = math.sqrt ((4*math.pow(3.14, 2)) / ((6.67 / math.pow (10,11)*(m1 + m2)) * math.pow(a,3)))

print(f'\nO valor do período orbital do corpo que orbita em volta da terra é {p}\n')