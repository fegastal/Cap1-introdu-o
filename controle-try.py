def main(args):
    # entramos com o divisor no teclado
    # a função int converte a string lida no teclado em um inteiro

    dividendo = 20

    numeroExperimentos = 5

    while numeroExperimentos > 0:

        divisor = int(input("Entre com um numero entre 0 e 10: "))

        try:
            resultado = dividendo / divisor
            print("Resultado= ", resultado)

        except:
            print("Erro: Divisão por zero!")


        finally:
            print("Passo sempre por aqui")
            numeroExperimentos -= 1

    print("\nÉ isso aí!")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


''' IOError: Se o arquivo não pode ser aberto.

ImportError : se o módulo não pode ser encontrado pelo interpretador Python.

ValueError: Ocorre se uma função recebe um argumento do tipo correto mas com valor inadequado.

KeyboardInterrupt: Gerada quando o usuário pressiona a tecla de interrupção, geralmente [ctrl] C.

EOFError: Gerada quando foi atingida uma condição de final de arquivo (EOF) sem ser lido nenhum dado.'''