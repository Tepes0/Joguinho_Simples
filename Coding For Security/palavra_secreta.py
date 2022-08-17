print("############# SEJA BEM VINDO(A) ############ \n ""############ AO PALAVRA SECRETA ############")


tentativa = input("Digite sua tentativa de palavra secreta aqui:")
palavra_secreta = ('pneumoultramicroscopicossilicovulcanoconiose ')

if tentativa == (palavra_secreta):
    print("Parabéns! Você acertou a palavra secreta que é:", (palavra_secreta))
else:
    print("ERRO - tente novamente, a palavra secreta não é:", (tentativa))
    print("Uma dica: a palavra tem +de 30 letras e é uma doença")