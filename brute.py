from random import *
import os
b = input('senha:')
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
  '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '|', '\\'
]

pw=""
while(pw!=b):
    pw=""
    for letter in range(len(b)):
        guess_pwd = pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print("tentando ", pw)
        print('descobrindo...')
        print("obrigado por usar minha ferramenta!")
        os.system("clear")
        
print("sua senha é: ", pw)

