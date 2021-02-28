from cnpj import valida, gera_um_novo_cnpj

if __name__ == "__main__":
    while True:
        action = input("Deseja válidar[1] ou gerar[2] um novo cnpj?\n-> ")
        action = int(action) if action.isdigit() else 0
        if action == 1:
            cnpj = input("Digite seu cnpj\n-> ")
            if valida(cnpj):
                print("Seu cnpj é valido\n")
            else:
                print("Seu cnpj não é válido\n")
        elif action == 2:
            print(f"Novo cnpj gerado\n-> {gera_um_novo_cnpj()}\n")
        else:
            print("Digite uma resposta válida\n")
