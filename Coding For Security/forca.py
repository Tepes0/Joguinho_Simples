print("############# SEJA BEM VINDO(A) ############ \n ""############ À FORCA ############")
print("Para começar, vamos te dar a dica... A palavra é uma cidade turística!\nBoa sorte!")
print(""
      ""
      "")

palavra = 'paranapiacaba'

acertos = 0
erros = 0
letras_certas = ''
letras_erradas = ''
#a seguir, inserindo o jogo dentro da função while para criar um ciclo que
#repete a pergunta a cada letra até finalizar a palavra, a partir do numero de chances que são 6.

while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for tentativa in palavra:
        if tentativa in letras_certas:
            mensagem += tentativa
        else:
            mensagem += '_ '
    print(mensagem)
    print("Essas são as letras que você errou:" + letras_erradas)

    tentativa = input("Digite seu chute aqui:")

    if tentativa in palavra:
        print("Muito Bem! Você acertou!")
        letras_certas += tentativa
        acertos += palavra.count(tentativa)
    else:
        print("Que pena! Você errou.")
        letras_erradas += tentativa
        erros += 1


























