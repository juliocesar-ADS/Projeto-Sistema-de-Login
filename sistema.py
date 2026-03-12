def cadastrar():

    usuario == input("Crie um usuário: ")
    senha == input("Crie uma senha: ")

    with open("logins.txt", "a") as arquivo:
        arquivo.write(usuario + "," + senha + "\n")

    print("Usuário cadastrado com sucesso!")

def login():

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    with open("logins.txt", "r") as arquivos:
        linhas = arquivo.readlines()

    login_encontrado = False

    for linha in linhas:

        linha = linha.strip()
        dados = linha.split()

        usuario_arquivo = dados[0]
        senha_arquivo = dados[1]

        if usuario == usuario_arquivo and senha == senha_arquivo:
            login_encontrado = True

    if login_encontrado:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos")

while True:

    print("\n1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        login()
        
    elif opcao == "3":
        print("Sistema encerrado")
        break
    else:
        print("Opção inválida")