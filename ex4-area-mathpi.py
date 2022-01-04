'''Exercício 04

A área de um triângulo é igual à metade do produto do comprimentos de um dos lados
pela distância ao vértice oposto medida perpendicularmente. Refira como podia
usar Python para calcular o valor concreto da área do triângulo, conhecidos aqueles valores.


a) Narrativa:

1. declarar as variáveis
2. solicitar ao utilizador o lado do hamburguer novo (L);
3. guardar o valor do lado do hamburguer novo;
4. solicitar ao utilizar o diâmetro do hamburguer antigo (D);
5. guardar o valor do diâmetro do hamburguer antigo;
6. calcular a área do hamburguer novo (A1);
7. devolver o valor da A1;
8. calcular a área do hamburguer antigo (A2);
9. devolver o valor da A2;
8. se A1 = A2: avisar ("trata-se da mesma quantidade de hamburguer anterior");
9. senão, avisar ("esse hamburguer não possui a mesma quantidade de carne picada que o antigo").

b) Pseudo-código:

Início
    Vars: L, D, A1, A2: int(float)
    Escrever ("Digite o valor do lado do hamburguer novo.")
    Ler (L)
    Escrever ("Digite o valor do diâmetro do hamburguer antigo.")
    Ler (D)
    A1 = L * L
    Ler (A1)
    A2 = [3,14 * (d/2)]
    Ler (A2)

    Se A1 = A2:
    Escrever ("Trata-se da mesma quantidade de hamburguer anterior.")
    Senão:
    Escrever ("Esse hamburguer não possui a mesma quantidade de carne picada que o antigo.")
Fim

'''
import math

print("Digite o valor do lado do hamburguer novo.")
L=float(input())

print("Digite o valor do diâmetro do hamburguer antigo.")
D=float(input())

A1 = (L*L)
A2 = ((math.pi)*(D/2))

if A1 == A2:
    print("Trata-se da mesma quantidade de hamburguer anterior.")
else:
    print("Esse hamburguer não possui a mesma quantidade de carne picada que o antigo.")