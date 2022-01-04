'''Exercício 04

Dada a fórmula do índice de massa corporal (IMC), desenvolva um programa que calcule-o.


a) Narrativa:

1. declarar as variáveis: p, h, res
2. solicitar ao utilizador o valor de seu peso (p) em kg;
3. guardar o valor do peso (p) em kg;
4. solicitar ao utilizador sua altura (h);
5. guardar o valor de sua altura (h);
6. calcular o valor do índice de massa corporal (res);
7. guardar o valor do índice de massa corporal (res);
8. devolver o valor do índice de massa corporal: "Seu índice de massa corporal é", res);

b) Pseudo-código:

Início
import math
    Vars: p, h, res: int(float)
    Escrever ("Digite o valor de seu peso (em kg).")
    Ler (p)
    Escrever ("Digite o valor de sua altura (em m).")
    Ler (h)

    res = [(p) / math.pow (h,2)]

    Escrever ("O valor de seu Índice de Massa Corporal é", res)
Fim

'''
import math

print("Digite o valor de seu peso (em kg).")
p=float(input())

print("Digite o valor de sua altura (em m).")
h=float(input())

res = (p) / math.pow (h,2)

print("O valor de seu Índice de Massa Corporal é", res)
