def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    LIMITE = 500

    contador = 0
    valor = 1 + contador
    while valor < LIMITE:
        print('El valor es: ' + str(valor))
        contador = contador + 1
        valor = 1 + contador
        if valor == 20:
            break


if __name__ == '__main__':
    run()