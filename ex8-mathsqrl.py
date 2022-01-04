'''Exercício 08

Importe o módulo math e experimente várias funções fornecidas. O que acontece se tentar calcular a raiz quadrada
de um inteiro negativo?

Traceback (most recent call last):
  File "C:\Users\liisb\PycharmProjects\pythonProject26\main.py", line 10, in <module>
    raiz = math.sqrt(num)
ValueError: math domain error'''

import math
num = float(input("Entre com um número:\n"))
raiz = math.sqrt(num)
print(f'\nA raiz quadrada de {num} é {raiz}\n')