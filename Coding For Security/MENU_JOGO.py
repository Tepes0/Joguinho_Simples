print("################### SEJAM BEM VINDOS ################## \n ""################## AO MENU DE JOGOS ###################")
print("*Jogos Disponíveis* \n 1 Numero Secreto \n 2 Palavra Secreta \n 3 Forca")
seleção = int(input("Número do jogo escolhido: "))


if seleção == (1):
    import importlib
    __import__(importlib.import_module("numero_secreto.py"))
if seleção == (2):
    import importlib
    __import__(importlib.import_module("palavra_secreta.py"))
if seleção == (3):
    import importlib
    __import__(importlib.import_module("forca.py"))


