'''Exercício 02

Suponha que tem uma sala retangular de dimensão 8 x 6. Admitindo que quer cobrir o chão com tijoleira de
2x2, calcule o número de unidades de que vai precisar.


a) Narrativa:

1. declarar as variáveis;
2. solicitar ao utilizador a altura e a largura da sala;
3. guardar o valor da altura e da largura em duas variáveis x1 e y1;
4. solicitar ao utilizador a altura e a largura da tijoleira x2 e y2;
4. fazer a operação de divisão entre essa as variáveis x1 e x2, e y1 e y2;
5. a partir dos dois resultados (x3 e y3), fazer uma multiplicação entre eles;
5. apresentar ao utilizador o resultado equivalente.

b) Pseudo-código:

Início
    Vars: x1, x2, x3, y1, y2, y3, res: int(float)
    Escrever ("Digite a o valor da altura e da largura da sala, respectivamente."
    Ler (x1 e y1)
    Escrever ("Digite a o valor da altura e da largura da tijoleira, respectivamente."
    Ler (x2 e y2)
    x3 <- (x1 / x2)
    y3 <- (y1 / y2)

    res <- (x3 * y3)
    Esc ("A resposta é:", res)
Fim

'''
import math

print("Digite a o valor da altura da sala.")
x1 =float(input())
print("Digite a o valor da largura da sala.")
y1 =float(input())

print("Digite a o valor da altura da tijoleira.")
x2 =float(input())
print("Digite a o valor da largura da tijoleira.")
y2 =float(input())

x3 = (x1 / x2)
y3 = (y1 / y2)
res = (x3 * y3)

print ("A quantidade de unidades é de", res)