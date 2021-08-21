def sanitizacao(numero):
    # for/foreach/while por cada caracter de numero
    # verificando se é 0 ou 1
    # caso não seja 0 ou 1 -> não atribuir esse número em nova variável
    # for 0 até tamanho do numero
    # se cursor == 0 ou == 1 -> outra_var = cursor
    # return outra_var
    aux = ''
    for x in numero:
        if x == '0' or x == '1':
            aux = aux + x

    return aux


def main ():
    b = 0
    while b == 0 or b == 1:
        b = str(input())
        b = sanitizacao(b)
        b = int(b, 2)

    print(b)
    
main()
