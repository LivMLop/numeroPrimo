# -*- coding: windows-1252 -*-
import os

a = True
while a:
    try:
        num = int(input("Insira um valor (-1) para sair: "))
        if num < -1:
            print('O valor {} é negativo. Insira um valor positivo.'.format(num))
        for i in range(num + 1):
            div = 0
            for x in range(1, i + 1):
                resto = i % x
                if resto == 0:
                    div += 1
            if div == 2:
                print('O número {} é primo.'.format(i))
            else:
                print('O número {} não é primo.'.format(i))
        if num == -1:
            a = False
            print("Encerrando aplicação. Obrigado.")
    except ValueError:
        os.system("cls")
        print('O valor {} não é válido.'.format(num))
        os.system("pause")
