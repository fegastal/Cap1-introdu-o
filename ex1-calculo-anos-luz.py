'''Exercício 01

A galáxia Andrômeda está a 2.9 milhões de anos-luz da Terra. Um ano luz equivale a 9.459 x 10^12 quilômetros.
A quantos quilômetros se encontra a galáxia da Terra?

a) Narrativa:

1. declarar as variáveis;
2. solicitar ao utilizador a distância em anos-luz que a galáxia Andrômeda encontra-se da galáxia da Terra. cuidado
com a unidade de medida;
3. guardar o valor distância em uma variável;
4. fazer a operação de multiplicação entre essa variável e os 9.459 x 10^12 quilômetros equivalente a 1 ano luz;
5. apresentar ao utilizador o resultado equivalente.

b) Pseudo-código:

Início
    Vars: x: int(float), res: int(float)
    Escrever ("Digite a distância em anos-luz que a galáxia Andrômeda se encontra da galáxia da Terra.\n
    /n Cuidado com a Unidade de medida!")
    Ler (x)
    Res <- ((9.459 x 10^12) * x)
    Esc ("A resposta é:", res)
Fim

'''
import math

print("Digite a distância em anos-luz que a galáxia Andrômeda se encontra da galáxia da Terra.")
print ("Cuidado com a unidade de medida, não utilizar a potenciação!")

x=float(input())
res = (9459000000000 * x)

print ("O valor distância é de", res)
