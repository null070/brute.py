from random import choice
import os

# Entrada da senha
b = input('Digite sua senha: ')

# Lista de caracteres possíveis
pwd = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
  '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '|', '\\'
]

pw = ""
while pw != b:
    pw = ""
    for _ in range(len(b)): 
        pw += choice(pwd) 
    print("Tentando:", pw)
    print("Descobrindo...")
    os.system("clear")

print("Senha encontrada:", pw)
