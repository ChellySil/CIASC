class TelaSistema:
    def mostra_opcoes(self):
        print("---------MENU-----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Usuario")
        print("2 - Logar como Usuario")
        print("0 - finalizar")
        opcoes = int(input("escolha uma opcao:"))
        return opcoes