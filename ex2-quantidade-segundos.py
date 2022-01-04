'''Exercício 02

Calcule o número de segundos que existe num ano normal (365 dias).

a) Narrativa:

1. declarar as variáveis;
2. solicitar ao utilizador a quantidade de dias em questão;
3. guardar o valor da quantidade em uma variável;
4. fazer a operação de multiplicação entre essa variável e 86.400 segundos (equivalente a um dia);'"
5. apresentar ao utilizador o resultado equivalente.

b) Pseudo-código:

Início
    Vars: x: int(float), res: int(float)
    Escrever ("Digite a quantidade de dias para calcular a quantidade de segundos em questão."
    Ler (x)
    Res <- (x * 86400)
    Esc ("A resposta é:", res)
Fim

'''
import math

print("Digite a quantidade de dias para calcular a quantidade de segundos em questão.")

x=float(input())
res = (x * 86400)

print ("A quantidade de segundos é de", res)