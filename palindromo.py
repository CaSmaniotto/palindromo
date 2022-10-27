def palindromo(palavra, ini, fin, meio):
    # caso de parada
    if ini < meio:
        if fin < meio:

            # se a letra no indice ini for igual a letra no indice fin, será feita chamada recusiva...
            if palavra[ini] == palavra[fin]:
                ini += 1
                fin -= 1
                palindromo(palavra, ini, fin, meio)

            # se forem diferentes a palavra não é palindromo
            else:
                print("Não é palindromo!")
                return 0
    print("É palindromo")
    return 1


palavra = input("Digite a palavra: ")

tam = 0

# descobrindo o tamanho da palavra
for i in range(len(palavra)):
    tam += 1

# numero que corresponde a letra do meio
meio = tam // 2
palindromo(palavra, 0, -1, meio)
