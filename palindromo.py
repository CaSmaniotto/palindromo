def palindromo(palavra, ini, fin, meio):
    # caso de parada
    if (ini < meio and fin > meio):

        # se a letra no indice ini for igual a letra no indice fin, será feita chamada recusiva...
        if palavra[ini] == palavra[fin]:
            ini += 1
            fin -= 1
            # chamada recursiva
            palindromo(palavra, ini, fin, meio)
            return 0

        # se forem diferentes a palavra não é palindromo
        else:
            print("Não é palindromo!")
            return 0

    print("É palindromo")
    return 0


palavra = input("Digite a palavra: ")

# descobrindo o tamanho da palavra
ultimo_char = len(palavra)

# numero que corresponde a letra do meio
meio = len(palavra) // 2

# call function
palindromo(palavra.lower(), 0, ultimo_char-1, meio)