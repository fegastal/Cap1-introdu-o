'''Exercício 07

Escreva um programa que lhe permita calcular o volume de um cone, conhecidos o raio da base r e a altura h.
O volume pode ser calculado pela fórmula que se segue:

v = ((math.pi)*(math.pow(r,2))*h) / 3


a) Narrativa:

1. declarar as variáveis: r, h, v: int(float);
2. solicitar ao utilizador o valor do raio do cone;
3. guardar o valor do raio (r) do cone;
4. solicitar ao utilizar o valor da altura do cone;
5. guardar o valor da altura (h) do cone;
6. devolver o valor do volume do cone: "O valor do volume do cone é", v);

b) Pseudo-código:

Início
import math
    Vars: r, h, v: int(float)
    Escrever ("Digite o valor do raio do cone.")
    Ler (r)
    Escrever ("Digite o valor da altura do cone.")
    Ler (h)
    v = ((math.pi)*(math.pow(r,2))*h) / 3
    Escrever ("O valor do volume do cone é", v)
Fim

'''
import math

r = eval(input("Digite o valor do raio do cone:"))

h = eval(input("Digite o valor da altura do cone:"))

v = ((math.pi)*(math.pow(r,2))* h) / 3

print("O valor do volume do cone é", v)