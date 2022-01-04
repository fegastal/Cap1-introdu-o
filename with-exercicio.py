def main(args):
    # entramos com o nome do arquivo txt a ser lido

    nomeArquivo = input("Entre com o nome do arquivo: ")
    
    with open(nomeArquivo) as arquivo:
        dados = arquivo.read()
        print(dados)

    print("\nÉ isso aí!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

