from getpass import getpass

while True:
    email = input("Digite um email: ")
    qtde_carac_email =len(email)
    
    if email.isdigit():
        condition_email1 ="@unisales.com"
        condition_email2 ="@unisales.com.br"
    else:
        print("email Negado")

    


    senha = getpass("Digite uma senha: ")
    # senha = input("Digite uma senha : ")  # para ver a senhas so comentar a linha 1 e linha 5
    qtde_carac_senha = len(senha)

    count_Ltr = 0
    count_LtrM = 0
    count_nums = 0

    for c in senha:
        if c.isalpha():
            count_Ltr += 1
        if c.isdigit():
            count_nums += 1
        if c.isupper():
            count_LtrM +=1
        
    
    erros = []
    if len(senha) < 8:
        erros.append("Senha deve conter pelo menos 8 caracteres!")
        if not count_Ltr:
            erros.append("Senha deve conter letras!")

        if not count_LtrM:
            erros.append("Senha deve conter letras maiusculas!")

        if not count_nums:
            erros.append("Senha deve conter números!")


    if erros:
        print("Erros de senha:")
        for e in erros:
            print("-", e)
    else:
        print("Senha OK")