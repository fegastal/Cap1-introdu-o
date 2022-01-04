'''Ex 10
Jogo do adivinha. Não consegui rodar o programa.'''

import random

def adivinha(tentativas):
    secreto = random.randint(0,100)
    for i in range(tentativas):
        numero = eval(input("O seu palpite sff: "))
        if numero == secreto:
            print("Uaaau, acertou!")
            return True
        elif numero > secreto:
            return False
        elif numero < secreto:
            return False
    else:
        print("Lamento muito, acabaram suas tentativas.")
        return False
    