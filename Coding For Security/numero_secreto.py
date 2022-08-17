print("############# SEJA BEM VINDO(A) ############ \n ""############ AO NÚMERO SECRETO ############")
tentativa = int(input("Digite sua tentativa de número secreto aqui:"))
numero_secreto = 1822

if tentativa == (1822):
    print("Parabéns! Você acertou o número secreto que é:", int(numero_secreto))
else:
    print("ERRO - tente novamente, o número secreto não é:", int(tentativa))
#Dica para aproximar o jogador do número correto
if tentativa <1822:
    print("A sua tentativa foi menor que o número secreto")
elif tentativa >1822:
    print("A sua tentativa foi maior que o número secreto")