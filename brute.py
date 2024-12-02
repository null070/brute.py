import threading
from random import choice
import os

print('ferramenta em desenvolvimento')
b = input('Digite sua senha: ')


pwd = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
  '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '|', '\\'
]

found = False  


def brute_force(thread_id):
    global found
    while not found:
        pw = ""
        for _ in range(len(b)):  # Gera tentativa do mesmo tamanho da senha
            pw += choice(pwd)  # Escolhe um caractere aleatório
        print(f"Thread-{thread_id} tentando: {pw}")
        
        if pw == b:
            found = True
            print(f"\nSenha encontrada pela Thread-{thread_id}: {pw}")
            os._exit(0)  # Encerra o programa imediatamente


try:
    num_threads = int(input("Quantas threads você deseja usar?(nao recomendavel menores que 10 e maiores que 50)"))
    if num_threads <= 0:
        raise ValueError("O número de threads deve ser maior que zero.")
except ValueError as e:
    print(f"Entrada inválida: {e}. Usando 1 thread como padrão.")
    num_threads = 1


threads = []

for i in range(num_threads):
    t = threading.Thread(target=brute_force, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

except KeyboardInterrupt:
    print("\n[!] Programa interrompido pelo usuário. Encerrando...")
    sys.exit(0)
