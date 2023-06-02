# Cadastro de usuários// Criar uma classe

class usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email 
# Cadastrar usuários - nome, idade e email

def cadastrar_usuarios():
    nome = input('Digite nome do usuario:')
    idade = int(input('Digite idade do usuario:'))
    email = input('Digite o email do usuario:')

 # Classe Usuário com os dados fornecidos

    novo_usuario = usuario(nome, idade, email)

# Retornando o novo usuário criado
    return novo_usuario

# Exibe os dados de um usuário

def exibir_usuario(usuario):
    print("Nome:", usuario.nome)
    print("Idade:", usuario.idade)
    print("Email:", usuario.email)

# Testar o cadastro de usuários

usuarios = []

while True:
    opcao = input("Deseja cadastrar um novo usuario? (S/N) ")

    if opcao.upper() == "S":
        novo_usuario = cadastrar_usuarios()
        usuarios.append(novo_usuario)
    else:
        break


# Exibindo os usuários cadastrados

print("\nUsuários cadastrados:")
for usuario in usuarios:
    exibir_usuario(usuario)
    print()