INDICE_EMAIL = 0


usuarios = {}


def exibirUsuario(nome):
    print(f"Nome: {nome}\tE-mail: {usuarios[nome][INDICE_EMAIL]}")


# H1
def cadastrarUsuario():
    global usuarios
    nomeRequisitado = input("Nome do usuário: ")
    emailRequisitado = input("E-mail do usuário: ")
    usuarios[nomeRequisitado] = [emailRequisitado]
    print(f"Usuário {nomeRequisitado} registrado com sucesso.")


# H2
def exibirUsuariosCadastro():
    global usuarios
    print()
    for nome in usuarios.keys():
        exibirUsuario(nome)
    print()

    
# H3
def exibirUsuariosAlfabetica():
    global usuarios
    print()
    nomesOrdenados = sorted(usuarios.keys())
    for nome in nomesOrdenados:
        exibirUsuario(nome)
    print()


# H4
def verificarPresenca():
    global usuarios
    nomeRequisitado = input("Usuário a ser verificado: ")
    if nomeRequisitado in usuarios:
        print("Usuário encontrado.")
    else:
        print("Usuário não encontrado.")


# H5
def removerUsuario():
    global usuarios
    emailRequisitado = input("E-mail do usuário a ser removido: ")
    for nome in usuarios.keys():
        if usuarios[nome][INDICE_EMAIL] == emailRequisitado:
            del usuarios[nome]
            print("Usuário removido.")

    print("Usuário não encontrado.")

# H6
def alterarNome():
    global usuarios
    emailRequisitado = input("E-mail do usuário: ")
    for nome in usuarios.keys():
        if usuarios[nome][INDICE_EMAIL] == emailRequisitado:
            del usuarios[nome]
            novoNome = input("Novo nome do usuário: ")
            usuarios[novoNome] = [emailRequisitado]
            print("Nome alterado.")
            return

    print("Usuário não encontrado.")


def escolherAcao():
    print("O que deseja fazer?")
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir usuários (ordem de cadastro)")
    print("3 - Exibir usuários (ordem alfabética)")
    print("4 - Buscar usuário")
    print("5 - Remover usuário")
    print("6 - Atualizar nome de usuário")
    escolha = int(input("> "))
    
    if escolha == 1:
        cadastrarUsuario()
    elif escolha == 2:
        exibirUsuariosCadastro()
    elif escolha == 3:
        exibirUsuariosAlfabetica()
    elif escolha == 4:
        verificarPresenca()
    elif escolha == 5:
        removerUsuario()
    elif escolha == 6:
        alterarNome()
    else:
        print("Escolha indisponível.")

    
def main():
  while (True):
    escolherAcao()


if __name__ == "__main__":
  main()
