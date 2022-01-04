'''Exercício 09

Crie uma solução genérica para a conversão de uma moeda para outra.

'''

import math

x = float(input("Introduza o valor que possui e deseja converter."))
y = float(input("Introduza o valor da taxa de câmbio para a moeda que deseja obter."))

z = x*y

print(f'\nO valor que possui na moeda convertida é de {z}\n')