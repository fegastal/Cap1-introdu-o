'''Exercício 06

Escreva um programa que lhe permita converter uma temperatura na escala Celsius (Tc) para a escala Fahrenheit (Tf),
baseando-se na fórmula:

Tf: ((9/5)*Tc) + 32


a) Narrativa:

1. declarar as variáveis: Tc, Tf: int(float)
2. solicitar ao utilizador o valor da temperatura na escala Celsius;
3. guardar o valor da temperatura (Tc);
4. devolver o valor em escala Fahrenheit: "O valor em escala Fahrenheit é", res);

b) Pseudo-código:

Início
import math
    Vars: C, F: int(float)
    Escrever ("Digite o valor da temperatura na escala Celsius.")
    Ler (C)
    F = ((9/5)*C) + 32
    Escrever ("O valor em escala Fahrenheit é", res)
Fim

'''

cel = eval(input("Digite o valor da temperatura na escala Celsius."))

fah = ((9/5)* cel) + 32

print("O valor em escala Fahrenheit é", fah)