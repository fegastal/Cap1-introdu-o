def main(args):
    # entramos com a idade no teclado
    # a função int converte a string lida no teclado em um inteiro

    idade = int(input("Quantos anos voce tem?"))

    # Se a idade for maior do que 16 anos, ja pode votar...

    if idade >= 16:
        print("Você já tem idade para votar. Escolha bem o melhor para o país\n")

    # Se a idade for maior do que 10 E menor do que 16 já pode estudar Python   

    elif idade > 10 and idade < 16:
        print("Você já tem idade para dominar o Python\n")

    # e se a idade for menor do que 10 é mais indicado ir ao parque   
    else:
        print("Deixe o video-game de lado e vá se divertir no parque\n")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))