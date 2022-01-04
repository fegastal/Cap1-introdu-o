def main(args):
    print("Operação  do while sozinho")
    var = 10

    while var > 0:
        print("Valor= ", var)
        var = var - 1
    
    print("\nOperação do while com um break")

    var = 10

    while var > 0:
        print("Valor= ", var)
        var = var - 1
        if var == 5:
            break

    print("\nOperação do while com um continue")
    print("Observe o que acontece com var igual a 5")
    var = 10

    while var > 0:
        var = var - 1
        if var == 5:
            continue
        print("Valor= ", var)

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))