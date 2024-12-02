from random import *
import os
b = input('senha:')
pwd = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pw=""
while(pw!=b):
    pw=""
    for letter in range(len(b)):
        guess_pwd = pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print('descobrindo...')
        os.system("clear")
print("sua senha é: ", pw)
