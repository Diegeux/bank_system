import autenticacao
import professor
import os

os.system("cls")
entrada= int(input("Olá! Seja bem vindo ao Sistema Escolar. Como você gostaria de se logar?\n 1 - Coordenador\n 2 - Professor "))
if entrada == 1:
    os.system("cls")
    autenticacao.autenticacao_coordenador()
elif entrada ==2:
    print("okay!")
else:
    print("Não há essa opção! Inicie o programa novamente!")





