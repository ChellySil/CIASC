class TelaUsuario:
    def cadastro_usuario_dados(self):
        print("------CADASTRO------")

        nome = input('nome:')
        email = input('email:')
        senha = input('senha:')
        telefone = input('telefone:')
        rg = input('rg:')
        cpf = input('cpf:')
        titulo = input('titulo:')

        return {'nome': nome, 'email': email, 'senha': senha, 'telefone': telefone, 'rg': rg, 'cpf': cpf,
                'titulo': titulo}