def main(args):
    # interagindo com as letras de uma string
    # e imprimindo uma a uma
    print("\n Interagindo com uma string")
    for letra in 'Caderno':
        print('Letra  :', letra)
        
    print("\nInteragindo com uma lista")
    # interagindo com uma lista

    microprocessadores = ['ATMEGA328', 'PIC18F84', 'Z80', '8085']

    for micro in microprocessadores:
        print('CPU :', micro)

    print("\nInteragindo sobre uma faixa de números")
    # interagindo sobre uma faixa de números
    # observe que o último valor impresso é 9, e não 10
    for num in range(1, 10):
        print("Número :", num)

    print("\nUtilizando o  <break>")
    # utilizando o break para sair do loop
    for num in range(1, 10):
        print("Número :", num)
        if num == 5:
            break

    print("\nUtiizando o <continue>")
    # utilizando o continue para sair do loop
    for num in range(1, 10):
        print("Número :", num)
        if num == 5:
            continue

    print("\nUtilizando o else")
    # utilizando a instrução else
    for num in range(1, 10):
        print("Número :", num)

    else:
        print("Número :", num + 1)

    print("É isso aí!")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))